# Generated by Django 3.2.3 on 2021-10-03 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Park', '0002_auto_20211003_0852'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='parkmanager',
            options={'verbose_name_plural': '园区管理员'},
        ),
        migrations.AlterModelOptions(
            name='street',
            options={'verbose_name_plural': '街道管理'},
        ),
        migrations.CreateModel(
            name='ParkLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50, verbose_name='标题')),
                ('Content', models.TextField(null=True, verbose_name='内容')),
                ('RecordDate', models.DateTimeField(auto_now_add=True, verbose_name='记录时间')),
                ('UpdateDate', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('Memo', models.TextField(default='无', verbose_name='备注')),
                ('Park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Park.park', verbose_name='园区')),
            ],
            options={
                'verbose_name_plural': '开发日志',
            },
        ),
    ]
