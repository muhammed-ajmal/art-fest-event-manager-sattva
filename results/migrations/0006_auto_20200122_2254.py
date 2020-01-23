# Generated by Django 2.2.9 on 2020-01-22 17:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('results', '0005_auto_20200122_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsresult',
            name='winner11',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner11', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='eventsresult',
            name='winner12',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner12', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='eventsresult',
            name='winner13',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner13', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='eventsresult',
            name='winner14',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner14', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='eventsresult',
            name='winner21',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner21', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='eventsresult',
            name='winner22',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner22', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='eventsresult',
            name='winner23',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner23', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='eventsresult',
            name='winner24',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner24', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='eventsresult',
            name='winner31',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner31', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='eventsresult',
            name='winner32',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner32', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='eventsresult',
            name='winner33',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner33', to='events.Participant'),
        ),
        migrations.AlterField(
            model_name='eventsresult',
            name='winner34',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='related_winner34', to='events.Participant'),
        ),
    ]
