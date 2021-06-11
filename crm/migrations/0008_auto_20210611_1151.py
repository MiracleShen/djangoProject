# Generated by Django 3.2.3 on 2021-06-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0007_auto_20210611_1133'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacthistory',
            name='Creator',
            field=models.CharField(default='沈承永', max_length=40, verbose_name='创建人'),
        ),
        migrations.AlterField(
            model_name='contacthistory',
            name='ContactType',
            field=models.CharField(choices=[('客户->我', '客户->我'), ('我->客户', '我->客户')], default='客户->我', max_length=8, null=True, verbose_name='联系类型'),
        ),
    ]
