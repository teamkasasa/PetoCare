# Generated by Django 3.2.5 on 2022-06-16 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_vetbooking_appo_full_date_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groomingbooking',
            name='appo_full_date_time',
            field=models.DateTimeField(blank='True', null='True'),
        ),
        migrations.AlterField(
            model_name='trainingbooking',
            name='appo_full_date_time',
            field=models.DateTimeField(blank='True', null='True'),
        ),
    ]