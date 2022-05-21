# Generated by Django 4.0.3 on 2022-04-11 15:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TierThree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investors_id', models.CharField(blank=True, max_length=50, null=True)),
                ('wallet_address', models.CharField(blank=True, max_length=500, null=True)),
                ('coin_used', models.CharField(blank=True, max_length=20, null=True)),
                ('amount_invested', models.IntegerField(blank=True, null=True)),
                ('roi', models.IntegerField(blank=True, null=True)),
                ('date_of_investment', models.DateTimeField()),
                ('date_of_maturity', models.CharField(blank=True, max_length=50, null=True)),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
