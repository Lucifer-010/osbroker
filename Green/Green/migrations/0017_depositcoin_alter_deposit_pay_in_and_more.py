# Generated by Django 4.2.7 on 2024-01-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Green', '0016_withdraw_account_name_withdraw_account_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositCoin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qrcode', models.URLField(default='www.default.com')),
                ('Coin', models.CharField(choices=[('SOL Solana Solana', 'SOL Solana Solana'), ('USDT Tether TRC20', 'USDT Tether TRC20'), ('LTC Litecoin', 'LTC Litecoin'), ('SHIB Shiba ERC20', 'SHIB Shiba ERC20'), ('ETH Ethereum ERC20', 'ETH Ethereum ERC20'), ('DOGE Dogecoin', 'DOGE Dogecoin'), ('BNB Binance coin Binance Smart Chain', 'BNB Binance coin Binance Smart Chain'), ('BTC Bitcoin ', 'BTC Bitcoin ')], default=1, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
        migrations.AlterField(
            model_name='deposit',
            name='pay_in',
            field=models.CharField(choices=[('SOL Solana Solana', 'SOL Solana Solana'), ('USDT Tether TRC20', 'USDT Tether TRC20'), ('LTC Litecoin', 'LTC Litecoin'), ('SHIB Shiba ERC20', 'SHIB Shiba ERC20'), ('ETH Ethereum ERC20', 'ETH Ethereum ERC20'), ('DOGE Dogecoin', 'DOGE Dogecoin'), ('BNB Binance coin Binance Smart Chain', 'BNB Binance coin Binance Smart Chain'), ('BTC Bitcoin ', 'BTC Bitcoin ')], default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='withdraw',
            name='wallet',
            field=models.CharField(blank=True, choices=[('SOL Solana Solana', 'SOL Solana Solana'), ('USDT Tether TRC20', 'USDT Tether TRC20'), ('LTC Litecoin', 'LTC Litecoin'), ('SHIB Shiba ERC20', 'SHIB Shiba ERC20'), ('ETH Ethereum ERC20', 'ETH Ethereum ERC20'), ('DOGE Dogecoin', 'DOGE Dogecoin'), ('BNB Binance coin Binance Smart Chain', 'BNB Binance coin Binance Smart Chain'), ('BTC Bitcoin ', 'BTC Bitcoin ')], default=1, max_length=200, null=True),
        ),
    ]
