# Generated by Django 5.0.1 on 2024-02-24 18:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity_user', '0006_rename_event_name_event_event_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customcharityuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customcharityuser',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='customcharityuser',
            name='password',
        ),
        migrations.RemoveField(
            model_name='customcharityuser',
            name='user_permissions',
        ),
    ]
