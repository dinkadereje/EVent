from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Event)
admin.site.register(models.Category)
admin.site.register(models.Country)
admin.site.register(models.City)
admin.site.register(models.Ticket)
admin.site.register(models.Registration)
