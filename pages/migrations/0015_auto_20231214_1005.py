# Generated by Django 3.2.1 on 2023-12-14 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_alter_appointment_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Appointment',
            new_name='Booking',
        ),
        migrations.RenameModel(
            old_name='Contact',
            new_name='MyContact',
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name_plural': 'Bookings'},
        ),
        migrations.AlterModelOptions(
            name='mycontact',
            options={'verbose_name_plural': 'My Contacts'},
        ),
    ]
