from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(Location)
admin.site.register(State)
admin.site.register(Region)

