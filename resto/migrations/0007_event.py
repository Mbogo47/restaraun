# Generated by Django 4.2.6 on 2023-11-29 11:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resto", "0006_galleryimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("title", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="events/")),
            ],
        ),
    ]
