# Generated by Django 2.2.9 on 2020-01-23 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0012_eventsresult_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventsresult',
            old_name='data',
            new_name='dataval',
        ),
    ]