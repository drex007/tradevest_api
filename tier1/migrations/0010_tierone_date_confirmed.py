# Generated by Django 3.2.8 on 2022-05-25 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tier1', '0009_alter_tierone_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tierone',
            name='date_confirmed',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
