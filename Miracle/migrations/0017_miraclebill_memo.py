# Generated by Django 3.2.3 on 2021-06-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Miracle', '0016_miraclenumber_organize'),
    ]

    operations = [
        migrations.AddField(
            model_name='miraclebill',
            name='Memo',
            field=models.TextField(default='1', verbose_name='备注'),
        ),
    ]