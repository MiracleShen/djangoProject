# Generated by Django 3.2.3 on 2021-07-22 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0010_oblist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='oblist',
            old_name='Number1',
            new_name='Phone1',
        ),
        migrations.RenameField(
            model_name='oblist',
            old_name='Number2',
            new_name='Phone2',
        ),
    ]
