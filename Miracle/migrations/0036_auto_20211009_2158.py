# Generated by Django 3.2.3 on 2021-10-09 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Miracle', '0035_miraclecredit_memo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='miracledid',
            options={'verbose_name_plural': '直线'},
        ),
        migrations.AlterModelOptions(
            name='miraclenumber',
            options={'verbose_name_plural': '码号'},
        ),
        migrations.AlterModelOptions(
            name='miraclepbx',
            options={'verbose_name_plural': '交换'},
        ),
    ]
