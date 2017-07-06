from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import stripe

from checkout.models import Payments

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    publishKey = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.userstripe.stripe_id

    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            customer = stripe.Customer.retrieve(customer_id)
            customer.sources.create(source=token)
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents
                currency="aud",
                customer=customer,
                description="Example charge"
            )

            p = Payments(
                charge_id=str(charge.id),
                amount=int(charge.amount),
                amount_refunded=int(charge.amount_refunded),
                application=str(charge.application),
                customer=str(charge.customer),
                paid=bool(charge.paid),
                receipt_number=str(charge.receipt_number),
                created=int(charge.created),
                status=str(charge.status))
            p.save()
        except stripe.error.CardError as e:
            # The card has been declined
            pass
    context = {'publishKey': publishKey}
    template = 'checkout.html'
    return render(request, template, context)
