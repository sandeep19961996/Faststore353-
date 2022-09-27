# Generated by Django 4.0.4 on 2022-08-07 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='order_date',
            new_name='ordered_date',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('M', 'MOBILE'), ('L', 'LAPTOP'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear'), ('AC', 'ACCESSORIES'), ('FO', 'FOOTWEAR')], max_length=2),
        ),
    ]
