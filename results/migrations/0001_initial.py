# Generated by Django 2.2.9 on 2020-01-22 14:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0021_auto_20200122_1931'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsResults',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Event')),
                ('participant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.Participant')),
            ],
            options={
                'ordering': ['-updated_on'],
            },
        ),
    ]
