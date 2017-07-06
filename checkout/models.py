from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.


class Payments(models.Model):
    customer = models.CharField(max_length=120)
    charge_id = models.CharField(max_length=120)
    amount = models.IntegerField()
    amount_refunded = models.IntegerField()
    application = models.CharField(max_length=120)
    time_created = models.DateField(auto_now=True)
    created = models.IntegerField()
    paid = models.BooleanField()
    receipt_number = models.CharField(max_length=120)
    status = models.CharField(max_length=120)

    def __unicode__(self):
        return self.charge_id

    class Meta:
        verbose_name_plural = "Payments"



