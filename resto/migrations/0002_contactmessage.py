# Generated by Django 4.2.6 on 2023-11-28 10:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resto", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
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
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=255)),
                ("message", models.TextField()),
            ],
        ),
    ]