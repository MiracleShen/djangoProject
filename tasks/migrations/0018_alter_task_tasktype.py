# Generated by Django 3.2.3 on 2021-07-20 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0017_alter_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='tasktype',
            field=models.CharField(choices=[('账务管理', '账务管理'), ('行政管理', '行政管理'), ('商机管理', '商机管理'), ('客户服务', '客户服务'), ('技术支持', '技术支持'), ('系统维护', '系统维护'), ('软件开发', '软件开发'), ('合伙人管理', '合伙人管理')], default='账务管理', max_length=8, verbose_name='任务类型'),
        ),
    ]
