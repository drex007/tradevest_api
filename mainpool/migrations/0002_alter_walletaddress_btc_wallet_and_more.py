# Generated by Django 4.0.4 on 2022-04-13 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpool', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walletaddress',
            name='btc_wallet',
            field=models.CharField(blank=True, default='bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='walletaddress',
            name='busd_wallet',
            field=models.CharField(blank=True, default='bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='walletaddress',
            name='litecoin_wallet',
            field=models.CharField(blank=True, default='bc1qxy2kgdygjrsqtzq2n0yrf2493p83kkfjhx0wlh', max_length=500, null=True),
        ),
    ]
