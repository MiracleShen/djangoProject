# Generated by Django 3.2.3 on 2021-06-11 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0013_alter_task_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'permissions': (('assign_task', '分配任务'),), 'verbose_name_plural': '任务管理'},
        ),
    ]
