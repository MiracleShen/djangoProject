# Generated by Django 3.2.3 on 2021-10-09 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Park', '0009_alter_park_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='park',
            name='Street',
        ),
        migrations.AddField(
            model_name='park',
            name='Town',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='乡镇'),
        ),
    ]
