# Generated by Django 4.2 on 2023-05-07 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_basket_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='user',
        ),
        migrations.AddField(
            model_name='basket',
            name='customer_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
