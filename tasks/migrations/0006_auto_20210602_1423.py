# Generated by Django 3.2.3 on 2021-06-02 06:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_alter_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='createdtime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='updatedtime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
