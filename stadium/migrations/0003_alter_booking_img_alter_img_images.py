# Generated by Django 5.1 on 2024-09-27 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stadium', '0002_alter_booking_hour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='img',
            field=models.ImageField(upload_to='./img'),
        ),
        migrations.AlterField(
            model_name='img',
            name='images',
            field=models.ImageField(upload_to='./img'),
        ),
    ]
