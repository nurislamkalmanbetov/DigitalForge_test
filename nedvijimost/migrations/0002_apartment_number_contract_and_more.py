# Generated by Django 4.2.11 on 2024-04-10 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nedvijimost', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='number_contract',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Номер контракта'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='phone_number_customer',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер телефона клиента'),
        ),
    ]
