# Generated by Django 5.1.2 on 2024-11-04 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels_app', '0002_remove_reservation_user_guest_reservation_guest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels_app.guest')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels_app.room')),
            ],
        ),
    ]
