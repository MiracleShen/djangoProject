# Generated by Django 3.2.3 on 2021-07-19 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_task_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Owner',
            field=models.CharField(choices=[('沈承永', '沈承永'), ('耿萌萌', '耿萌萌')], default='沈承永', max_length=40, verbose_name='执行人'),
        ),
    ]