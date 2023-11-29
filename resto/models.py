from django.db import models

class Booking(models.Model):
    booking_name = models.CharField(max_length=255)
    booking_email = models.EmailField()
    booking_phone = models.CharField(max_length=15)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    booking_people = models.PositiveIntegerField()
    booking_message = models.TextField()

    def __str__(self):
        return self.booking_name

class ContactMessage(models.Model):
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_subject = models.CharField(max_length=255)
    contact_message = models.TextField()

    def __str__(self):
        return f"{self.contact_name} - {self.contact_subject}"

class Chef(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    image = models.ImageField(upload_to='chefs/')
    twitter_link = models.URLField(blank=True, null=True)
    facebook_link = models.URLField(blank=True, null=True)
    instagram_link = models.URLField(blank=True, null=True)
    linkedin_link = models.URLField(blank=True, null=True)
    bio = models.TextField()

    def __str__(self):
        return self.name