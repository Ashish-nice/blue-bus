# Generated by Django 5.1.6 on 2025-02-11 10:00

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bus_booking", "0002_alter_bus_options_remove_bus_bus_destination_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bus",
            options={"verbose_name": "Bus", "verbose_name_plural": "Buses"},
        ),
        migrations.AlterField(
            model_name="bus",
            name="bus_route",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=50), size=8
            ),
        ),
        migrations.AlterField(
            model_name="bus",
            name="bus_seats_available",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
