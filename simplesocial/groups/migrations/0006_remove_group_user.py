# Generated by Django 4.1.7 on 2023-03-04 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_group_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='user',
        ),
    ]
