# Generated by Django 2.2.9 on 2020-01-07 14:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200107_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999999999'. Up to 10 digits allowed.", regex='^[0-9]{10}$')]),
        ),
    ]
