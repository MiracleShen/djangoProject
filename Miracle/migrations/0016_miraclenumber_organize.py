# Generated by Django 3.2.3 on 2021-06-01 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    # dependencies = [
    #     ('Miracle', '0015_alter_miraclenumber_unique_together'),
    # ]

    operations = [
        migrations.AddField(
            model_name='miraclenumber',
            name='Organize',
            field=models.CharField(default=' ', max_length=30, verbose_name='客户名称'),
        ),
    ]
