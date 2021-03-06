# Generated by Django 3.2.3 on 2021-08-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0016_oblist_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oblist',
            name='Owner',
            field=models.CharField(choices=[('沈承永', '沈承永'), ('耿萌萌', '耿萌萌'), ('王忠盟', '王忠盟')], default='沈承永', max_length=40, verbose_name='执行人'),
        ),
        migrations.AlterField(
            model_name='oblist',
            name='Phone2',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='号码2'),
        ),
        migrations.AlterField(
            model_name='oblist',
            name='Status',
            field=models.CharField(choices=[('未联系', '未联系'), ('未接通', '未接通'), ('拒绝沟通', '拒绝沟通'), ('再联系', '再联系'), ('有意向', '有意向'), ('有需求', '有需求')], default='未联系', max_length=20, verbose_name='状态'),
        ),
    ]
