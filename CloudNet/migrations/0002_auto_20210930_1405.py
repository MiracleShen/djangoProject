# Generated by Django 3.2.3 on 2021-09-30 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CloudNet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SN', models.CharField(max_length=19, verbose_name='SN码')),
                ('Mac', models.CharField(max_length=17, verbose_name='Mac地址')),
                ('RecordDate', models.DateTimeField(auto_now_add=True, verbose_name='记录时间')),
                ('UpdateDate', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('Memo', models.TextField(default='库存', verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': 'CPE设备',
            },
        ),
        migrations.AlterField(
            model_name='card',
            name='Memo',
            field=models.TextField(default='库存', verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='card',
            name='Operator',
            field=models.CharField(choices=[('中国电信', '中国电信'), ('中国联通', '中国联通'), ('中国移动', '中国移动'), ('中国铁通', '中国铁通')], default='中国电信', max_length=12, verbose_name='运营商'),
        ),
    ]
