# Generated by Django 4.2.7 on 2023-12-31 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Green', '0009_rename_mytrades_copiedtrade_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='walletbalance',
            old_name='balance',
            new_name='trading_balance',
        ),
        migrations.AddField(
            model_name='walletbalance',
            name='binance_coin_mining',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='walletbalance',
            name='bitcoin_mining',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='walletbalance',
            name='cosmos_mining',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='walletbalance',
            name='dogecoin_mining',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='walletbalance',
            name='ethereum_mining',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=999),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='walletbalance',
            name='verified',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(auto_now_add=True)),
                ('otp', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-time',),
            },
        ),
    ]