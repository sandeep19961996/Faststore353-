# Generated by Django 4.0.4 on 2022-08-28 14:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_customer_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='product_slug',
        ),
    ]
