from django.contrib import admin
from .models import CarModel
from django.contrib.auth.models import Group
# Register your models here.

admin.site.register(CarModel)
admin.site.unregister(Group)
