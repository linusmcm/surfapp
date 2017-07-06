from django.http import HttpResponse
from django.template import loader
from profiles.models import profile
from .models import *


def location(request):
    template = loader.get_template('location.html')
    context = {
        'country': Country.objects.all(),
    }
    return HttpResponse(template.render(context, request))


def locationMap(request, id):
    template = loader.get_template('locationMap.html')
    context = {
        'location': Location.objects.get(id=id),
        'profiles': profile.objects.get(my_locations=id),
    }
    return HttpResponse(template.render(context, request))

