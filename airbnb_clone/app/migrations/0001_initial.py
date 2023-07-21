# Generated by Django 4.2.3 on 2023-07-20 16:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Place",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "display_image",
                    models.FileField(upload_to="images/", verbose_name="Display Image"),
                ),
                ("location", models.CharField(max_length=100, verbose_name="Location")),
                ("price", models.IntegerField(verbose_name="Price")),
                ("rating", models.FloatField(verbose_name="Rating")),
                ("guest_capacity", models.IntegerField(verbose_name="Guest Capacity")),
                ("bedrooms", models.IntegerField(verbose_name="Bedrooms")),
                ("beds", models.IntegerField(verbose_name="Beds")),
                ("bathrooms", models.IntegerField(verbose_name="Bathrooms")),
                ("has_wifi", models.BooleanField(verbose_name="Has Wifi")),
                ("has_tv", models.BooleanField(verbose_name="Has TV")),
                ("is_available", models.BooleanField(verbose_name="Is Available")),
                (
                    "is_self_check_in",
                    models.BooleanField(verbose_name="Is Self Check In"),
                ),
                (
                    "is_pet_friendly",
                    models.BooleanField(verbose_name="Is Pet Friendly"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="State",
            fields=[
                (
                    "name",
                    models.CharField(
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="Name",
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.country",
                        verbose_name="Country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Views",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
            ],
        ),
        migrations.CreateModel(
            name="Village",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="Name")),
                (
                    "state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.state",
                        verbose_name="State",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created At"),
                ),
                ("start_datetime", models.DateTimeField(verbose_name="Start Datetime")),
                ("end_datetime", models.DateTimeField(verbose_name="End Datetime")),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.place",
                        verbose_name="Place",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="place",
            name="views",
            field=models.ManyToManyField(
                related_name="views", to="app.views", verbose_name="Views"
            ),
        ),
        migrations.AddField(
            model_name="place",
            name="village",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="app.village",
                verbose_name="Village",
            ),
        ),
    ]