# Generated by Django 4.2.6 on 2023-11-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resto", "0008_menucategory_menuitem"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("author_name", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("image", models.ImageField(upload_to="testimonials/")),
                ("stars", models.PositiveIntegerField()),
            ],
        ),
    ]
