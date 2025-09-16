from django.contrib import admin
from .models import CommunityList, Bike, Event
# Register your models here.

admin.site.register(CommunityList)
admin.site.register(Bike)
admin.site.register(Event)