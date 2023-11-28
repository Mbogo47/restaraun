# from django.shortcuts import render
# from .models import Booking, ContactMessage

# # Create your views here.
# def index(request):
#     return render(request, 'index.html')

# def contact(request):
#     contactus = ContactMessage.objects.all()
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         subject = request.POST['subject']
#         message= request.POST['message']
#         contact = ContactMessage(name=name, email=email, subject=subject, message=message)
#         contact.save()
#         context = {
#             'contactus': contactus
#         }
#     return render(request, 'contact.html', context)


# def booking(request):
#     bookings = Booking.objects.all()
#     if request.method == 'POST':
#         name = request.POST['name']
#         email = request.POST['email']
#         phone= request.POST['phone']
#         date = request.POST['date']
#         time = request.POST['time']
#         people = request.POST['people']
#         message = request.POST['message']
#         booking = Booking(name=name, email=email, phone=phone, date=date, time=time, people=people, message=message)
#         booking.save()
#         context = {
#             'bookings': bookings
#         }
#     return render(request, 'booking.html', context)

from django.shortcuts import render
from .models import Booking, ContactMessage

def index(request):
    # Load existing data for the page
    contactus = ContactMessage.objects.all()
    bookings = Booking.objects.all()

    # Handle Contact Form Submission
    if request.method == 'POST' and 'contact_submit' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        contact = ContactMessage(name=name, email=email, subject=subject, message=message)
        contact.save()
        contactus = ContactMessage.objects.all()  # Refresh the data after submission

    # Handle Booking Form Submission
    elif request.method == 'POST' and 'booking_submit' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        people = request.POST['people']
        message = request.POST['message']
        booking = Booking(name=name, email=email, phone=phone, date=date, time=time, people=people, message=message)
        booking.save()
        bookings = Booking.objects.all()  # Refresh the data after submission

    context = {
        'contactus': contactus,
        'bookings': bookings,
    }

    return render(request, 'index.html', context)
