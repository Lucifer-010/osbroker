# Generated by Django 4.2.7 on 2023-12-31 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Green', '0013_withdraw'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpenClosedTrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ammount', models.DecimalField(decimal_places=2, max_digits=999)),
                ('up', models.DecimalField(decimal_places=2, max_digits=999)),
                ('down', models.DecimalField(decimal_places=2, max_digits=999)),
                ('pair', models.CharField(default='BTCUSD', max_length=500)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
