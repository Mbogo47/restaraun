from django.contrib import admin

# Register your models here.
from .models import Booking, ContactMessage, Chef

admin.site.register(Booking)
admin.site.register(ContactMessage)
admin.site.register(Chef)