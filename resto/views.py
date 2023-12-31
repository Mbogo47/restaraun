from django.shortcuts import render, redirect
from .models import Booking, ContactMessage, Chef, GalleryImage, Event, MenuItem, MenuCategory, Testimonial
from django.contrib import messages

def index(request):   
    chefs_list = Chef.objects.all()
    images = GalleryImage.objects.all()
    events_list = Event.objects.all()
    categories = MenuCategory.objects.all()
    menu_items = MenuItem.objects.all()
    testimonials = Testimonial.objects.all()
    print(testimonials)
    context = {'images': images,
               'chefs_list': chefs_list,
               'events_list': events_list,
               'categories': categories, 
               'menu_items': menu_items,
               'testimonials': testimonials
               }
    return render(request, 'index.html', context)

def booking(request):
    if request.method == 'POST':        
        booking_name = request.POST['booking_name']
        booking_email = request.POST['booking_email']
        booking_phone = request.POST['booking_phone']
        booking_date = request.POST['booking_date']
        booking_time = request.POST['booking_time']
        booking_people = request.POST['booking_people']
        booking_message = request.POST['booking_message']
        booking = Booking(booking_name=booking_name, booking_email=booking_email, booking_phone=booking_phone, booking_date=booking_date, booking_time=booking_time, booking_people=booking_people, booking_message=booking_message)
        booking.save()
        messages.success(request, 'Booking message sent successfully')
        return redirect('index') 
    return render(request, 'book.html')

def contact(request):
    if request.method == 'POST' :
        contact_name = request.POST['contact_name']
        contact_email = request.POST['contact_email']
        contact_subject = request.POST['contact_subject']
        contact_message = request.POST['contact_message']
        contact = ContactMessage(contact_name=contact_name, contact_email=contact_email, contact_subject=contact_subject, contact_message=contact_message)
        contact.save()
        messages.success(request, 'Contact message sent successfully')
        return redirect('index') 
    return render(request, 'contact.html')

