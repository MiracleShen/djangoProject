# Generated by Django 3.2.3 on 2021-10-03 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Park', '0003_auto_20211003_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='park',
            name='XY',
            field=models.CharField(max_length=50, null=True, verbose_name='坐标'),
        ),
    ]
