# Generated by Django 3.2.3 on 2021-10-06 22:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Park', '0008_alter_parklog_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='park',
            options={'ordering': ['id'], 'verbose_name_plural': '园区'},
        ),
    ]
