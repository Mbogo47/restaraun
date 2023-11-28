from django.contrib import admin

# Register your models here.
from .models import Booking, ContactMessage

admin.site.register(Booking)
admin.site.register(ContactMessage)