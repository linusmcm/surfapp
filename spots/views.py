from django.shortcuts import render

# Create your views here.
def new_spot(request):
    context = locals()
    template = 'new_spot.html'
    return render(request, template, context)

def my_spot(request):
    context = locals()
    template = 'my_spot.html'
    return render(request, template, context)