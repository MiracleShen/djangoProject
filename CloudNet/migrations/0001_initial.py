# Generated by Django 3.2.3 on 2021-09-29 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardNumber', models.CharField(max_length=19, verbose_name='卡号')),
                ('Operator', models.CharField(choices=[('中国电信', '中国电信'), ('中国联通', '中国联通'), ('中国移动', '中国移动'), ('中国铁通', '中国铁通')], max_length=12, verbose_name='运营商')),
                ('RecordDate', models.DateTimeField(auto_now_add=True, verbose_name='记录时间')),
                ('UpdateDate', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('Memo', models.TextField(default='1', verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '物联网卡',
            },
        ),
    ]