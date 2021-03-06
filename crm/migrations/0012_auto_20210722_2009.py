# Generated by Django 3.2.3 on 2021-07-22 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0011_auto_20210722_1956'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='oblist',
            options={'verbose_name_plural': '外呼名单'},
        ),
        migrations.AddField(
            model_name='oblist',
            name='Campaign',
            field=models.CharField(default='Miracle', max_length=20, verbose_name='战役'),
        ),
        migrations.AlterField(
            model_name='oblist',
            name='Phone1',
            field=models.CharField(max_length=11, verbose_name='号码1'),
        ),
        migrations.AlterField(
            model_name='oblist',
            name='Status',
            field=models.CharField(default='未联系', max_length=20, verbose_name='状态'),
        ),
    ]
