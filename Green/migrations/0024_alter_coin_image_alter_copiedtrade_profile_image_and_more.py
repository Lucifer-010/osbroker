# Generated by Django 4.2.11 on 2024-06-19 04:08

from django.db import migrations, models
import storages.backends.s3


class Migration(migrations.Migration):

    dependencies = [
        ('Green', '0023_openclosedtrade_loss_or_gain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='image',
            field=models.ImageField(storage=storages.backends.s3.S3Storage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='copiedtrade',
            name='profile_image',
            field=models.ImageField(storage=storages.backends.s3.S3Storage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='copytrader',
            name='profile_image',
            field=models.ImageField(storage=storages.backends.s3.S3Storage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='depositcoin',
            name='qrcode',
            field=models.ImageField(storage=storages.backends.s3.S3Storage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='market',
            name='image',
            field=models.ImageField(storage=storages.backends.s3.S3Storage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(storage=storages.backends.s3.S3Storage(), upload_to=''),
        ),
        migrations.AlterField(
            model_name='watchlist',
            name='image',
            field=models.ImageField(storage=storages.backends.s3.S3Storage(), upload_to=''),
        ),
    ]
