# Generated by Django 4.2.6 on 2023-11-28 11:23

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("resto", "0002_contactmessage"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="date",
            new_name="booking_date",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="email",
            new_name="booking_email",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="message",
            new_name="booking_message",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="name",
            new_name="booking_name",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="people",
            new_name="booking_people",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="phone",
            new_name="booking_phone",
        ),
        migrations.RenameField(
            model_name="booking",
            old_name="time",
            new_name="booking_time",
        ),
        migrations.RenameField(
            model_name="contactmessage",
            old_name="email",
            new_name="contact_email",
        ),
        migrations.RenameField(
            model_name="contactmessage",
            old_name="message",
            new_name="contact_message",
        ),
        migrations.RenameField(
            model_name="contactmessage",
            old_name="name",
            new_name="contact_name",
        ),
        migrations.RenameField(
            model_name="contactmessage",
            old_name="subject",
            new_name="contact_subject",
        ),
    ]
