# Generated by Django 3.2.3 on 2021-09-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Miracle', '0028_alter_miracleorders_customername'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miracleorders',
            name='API_Type',
            field=models.CharField(choices=[('无', '无'), ('有', '有')], default='无', max_length=10, verbose_name='API许可'),
        ),
        migrations.AlterField(
            model_name='miracleorders',
            name='APP_Number',
            field=models.IntegerField(default=0, verbose_name='APP许可数'),
        ),
        migrations.AlterField(
            model_name='miracleorders',
            name='CC_Number',
            field=models.IntegerField(default=0, verbose_name='轻客服许可数'),
        ),
        migrations.AlterField(
            model_name='miracleorders',
            name='Log_Number',
            field=models.IntegerField(default=0, verbose_name='录音许可数'),
        ),
        migrations.AlterField(
            model_name='miracleorders',
            name='MCU_Type',
            field=models.CharField(choices=[('无', '无'), ('有', '有')], default='无', max_length=10, verbose_name='多方通话许可'),
        ),
        migrations.AlterField(
            model_name='miracleorders',
            name='PBX_Type',
            field=models.CharField(choices=[('免费版', '免费版'), ('查询版', '查询版'), ('管理版', '管理版'), ('本地部署版', '本地部署版')], default='免费版', max_length=10, verbose_name='交换机类型'),
        ),
        migrations.AlterField(
            model_name='miracleorders',
            name='SIP_Number',
            field=models.IntegerField(default=0, verbose_name='SIP许可数'),
        ),
    ]
