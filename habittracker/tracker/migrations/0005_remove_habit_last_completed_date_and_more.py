# Generated by Django 5.1.2 on 2024-11-20 13:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_habit_last_completed_date_habit_reminder_frequency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='last_completed_date',
        ),
        migrations.RemoveField(
            model_name='habit',
            name='reminder_frequency',
        ),
        migrations.AlterField(
            model_name='habit',
            name='status',
            field=models.CharField(choices=[('ongoing', 'Ongoing'), ('not-completed', 'Not Completed'), ('finished', 'Finished')], default='ongoing', max_length=20),
        ),
        migrations.AlterField(
            model_name='habitcompletion',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.habit'),
        ),
        migrations.AlterField(
            model_name='habitstreak',
            name='habit',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tracker.habit'),
        ),
    ]
