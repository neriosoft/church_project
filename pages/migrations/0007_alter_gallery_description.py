# Generated by Django 4.2.6 on 2023-11-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pages", "0006_alter_event_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallery",
            name="description",
            field=models.CharField(max_length=255),
        ),
    ]
