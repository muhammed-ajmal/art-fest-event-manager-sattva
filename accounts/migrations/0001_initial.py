# Generated by Django 2.2.9 on 2020-01-07 13:51

import accounts.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.IntegerField(choices=[(0, 'Participant'), (1, 'Volunteer'), (2, 'Branch Captian'), (3, 'Admin'), (4, 'Visitor')], default=0)),
                ('branch', models.IntegerField(choices=[(0, 'CE'), (1, 'CS'), (2, 'EC'), (3, 'EEE'), (4, 'IT'), (5, 'ME'), (6, 'MCA'), (7, 'Branch/Dept')], default=7)),
                ('semester', models.IntegerField(choices=[(0, 'S1'), (1, 'S2'), (2, 'S3'), (3, 'S4'), (4, 'S5'), (5, 'S6'), (6, 'S7'), (7, 'S8'), (8, 'Semester')], default=8)),
                ('profile', models.ImageField(default='profile.png', help_text='Profile Picture', upload_to=accounts.models.user_directory_path)),
                ('contact', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('location', models.CharField(blank=True, default='CUCEK', help_text='eg:- College Name, organization name ..etc', max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
