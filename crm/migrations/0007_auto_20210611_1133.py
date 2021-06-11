# Generated by Django 3.2.3 on 2021-06-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20210610_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacthistory',
            name='ContactMedia',
        ),
        migrations.AddField(
            model_name='contacthistory',
            name='ContactType',
            field=models.CharField(choices=[('请求', '请求'), ('响应', '响应')], max_length=8, null=True, verbose_name='联系类型'),
        ),
    ]
