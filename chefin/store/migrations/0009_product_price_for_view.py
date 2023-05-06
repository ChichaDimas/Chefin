# Generated by Django 4.2 on 2023-05-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_for_view',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True),
        ),
    ]
