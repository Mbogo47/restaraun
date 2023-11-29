from django.contrib import admin

# Register your models here.
from .models import Booking, ContactMessage, Chef, GalleryImage, Event, MenuCategory, MenuItem

admin.site.register(Booking)
admin.site.register(ContactMessage)
admin.site.register(Chef)
admin.site.register(GalleryImage)
admin.site.register(Event)
admin.site.register(MenuCategory)
admin.site.register(MenuItem)