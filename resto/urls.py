from django.urls import path
from .views import index, booking, contact, chefs

urlpatterns = [
    path('', index, name='index'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),
    path('chefs/', chefs, name='chefs')
]
