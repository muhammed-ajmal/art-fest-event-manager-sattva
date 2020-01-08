# Generated by Django 2.2.9 on 2020-01-07 15:15

import ckeditor_uploader.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('venue', models.IntegerField(choices=[(0, 'Scheduled'), (1, 'Draft'), (2, 'Withdrawn'), (3, 'Stage 1'), (4, 'Stage 2'), (5, 'Stage 3'), (6, 'Stage 4'), (7, 'Stage 5'), (8, 'Stage 6')], default=1)),
                ('cover', models.ImageField(default='defaultevent.jpg', upload_to=events.models.user_directory_path)),
                ('about', ckeditor_uploader.fields.RichTextUploadingField()),
                ('max_participants', models.IntegerField(default=0)),
                ('slug', models.SlugField(help_text='WARNING : Use the same slug for while creating a Terms about events', max_length=200, unique=True)),
                ('scheduler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_auth', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['-updated_on'],
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('branch', models.IntegerField(choices=[(0, 'CE'), (1, 'CS'), (2, 'EC'), (3, 'EEE'), (4, 'IT'), (5, 'ME'), (7, 'Branch/Dept')], default=7)),
                ('semester', models.IntegerField(choices=[(0, 'S1'), (1, 'S2'), (2, 'S3'), (3, 'S4'), (4, 'S5'), (5, 'S6'), (6, 'S7'), (7, 'S8'), (8, 'Semester')], default=8)),
                ('regnumber', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="reg number must be entered in the format: '12180222'. Up to 8 digits allowed.", regex='^[0-9]{8}$')])),
                ('contact', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '999999999'. Up to 10 digits allowed.", regex='^[0-9]{10}$')])),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events_listed', to='events.Event')),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
    ]
