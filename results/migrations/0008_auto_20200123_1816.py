# Generated by Django 2.2.9 on 2020-01-23 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0007_auto_20200123_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchpoint',
            name='score',
            field=models.FloatField(),
        ),
    ]
