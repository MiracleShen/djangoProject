# Generated by Django 3.2.3 on 2021-10-05 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Park', '0004_park_xy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park',
            name='XY',
        ),
        migrations.AddField(
            model_name='park',
            name='Address',
            field=models.CharField(max_length=50, null=True, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='park',
            name='Street',
            field=models.CharField(max_length=50, null=True, verbose_name='所属街道'),
        ),
    ]