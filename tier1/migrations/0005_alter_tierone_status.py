# Generated by Django 3.2.8 on 2022-05-22 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tier1', '0004_alter_tierone_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tierone',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
