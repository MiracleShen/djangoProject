# Generated by Django 3.2.3 on 2021-06-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_alter_task_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='User',
            field=models.CharField(default='匿名', max_length=40, verbose_name='用户'),
        ),
    ]
