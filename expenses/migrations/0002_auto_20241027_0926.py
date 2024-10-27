# Generated by Django 3.2.25 on 2024-10-27 09:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='created_at',
        ),
        migrations.AddField(
            model_name='expense',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]