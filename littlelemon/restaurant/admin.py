from django.contrib import admin
from .models import Menu, Booking

# Registering the models with the admin site
admin.site.register(Menu)
admin.site.register(Booking)