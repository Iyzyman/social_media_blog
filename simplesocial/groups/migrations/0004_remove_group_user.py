# Generated by Django 4.1.7 on 2023-02-26 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_alter_group_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
    ]
