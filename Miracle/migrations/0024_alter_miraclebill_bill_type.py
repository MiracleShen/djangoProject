# Generated by Django 3.2.3 on 2021-06-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Miracle', '0023_alter_miracleorders_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miraclebill',
            name='Bill_Type',
            field=models.CharField(choices=[('租金', '租金'), ('话费', '话费')], default='租金', max_length=2, verbose_name='账单类型'),
        ),
    ]