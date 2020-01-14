# Generated by Django 2.2.9 on 2020-01-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_auto_20200113_0218'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='deletable',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='branch',
            field=models.IntegerField(choices=[(0, 'CE'), (1, 'CS'), (2, 'EC'), (3, 'EEE'), (4, 'IT'), (5, 'ME'), (6, 'MCA'), (7, 'Branch/Dept')], default=7),
        ),
        migrations.AlterField(
            model_name='participant',
            name='participant_type',
            field=models.IntegerField(choices=[(0, 'Main Participant'), (1, 'Accompanying Participant')], default=0),
        ),
        migrations.AlterField(
            model_name='participant',
            name='semester',
            field=models.IntegerField(choices=[(1, 'S2'), (3, 'S4'), (5, 'S6'), (7, 'S8'), (8, 'Semester')], default=8),
        ),
    ]
