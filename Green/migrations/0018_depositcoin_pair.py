# Generated by Django 4.2.7 on 2024-01-13 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Green', '0017_depositcoin_alter_deposit_pay_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='depositcoin',
            name='pair',
            field=models.CharField(default='wallet Address', max_length=500),
        ),
    ]
