# Generated by Django 4.2.7 on 2024-01-01 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Green', '0014_openclosedtrade'),
    ]

    operations = [
        migrations.AddField(
            model_name='openclosedtrade',
            name='trade_type',
            field=models.CharField(choices=[('OPEN TRADE', 'OPEN TRADE'), ('CLOSED TRADE', 'CLOSED TRADE')], default=1, max_length=500),
        ),
    ]