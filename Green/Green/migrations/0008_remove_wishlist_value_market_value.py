# Generated by Django 4.2.7 on 2023-12-30 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Green', '0007_alter_market_form_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='value',
        ),
        migrations.AddField(
            model_name='market',
            name='value',
            field=models.DecimalField(decimal_places=6, default=234.4343, max_digits=999),
            preserve_default=False,
        ),
    ]
