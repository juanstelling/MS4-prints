# Generated by Django 3.1.7 on 2021-03-31 15:50

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone_number',
            field=phone_field.models.PhoneField(max_length=31),
        ),
    ]
