from django.urls import path
from .views import index, booking, contact

urlpatterns = [
    path('', index, name='index'),
    path('booking/', booking, name='booking'),
    path('contact/', contact, name='contact'),

]
