# Generated by Django 2.2.9 on 2020-01-08 19:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_participant_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.IntegerField(choices=[(0, 'Individual'), (1, 'Group')], default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='regnumber',
            field=models.CharField(blank=True, max_length=8, validators=[django.core.validators.RegexValidator(message="reg number must be entered in the format: '12180222'. Up to 8 digits allowed.", regex='^[0-9]{8}$')]),
        ),
    ]
