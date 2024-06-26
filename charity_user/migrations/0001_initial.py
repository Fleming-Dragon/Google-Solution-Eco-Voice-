# Generated by Django 5.0.1 on 2024-02-18 15:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=100)),
                ('blog_heading', models.CharField(max_length=100)),
                ('blog_description', models.TextField()),
                ('uploaded_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donation_id', models.CharField(max_length=100)),
                ('donaor', models.CharField(max_length=100)),
                ('beneficiary', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
                ('date', models.DateField()),
                ('trancaction_method', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('event_id', models.IntegerField(unique=True)),
                ('event_address', models.CharField(max_length=100)),
                ('event_city', models.CharField(max_length=100)),
                ('event_state', models.CharField(max_length=100)),
                ('event_host', models.CharField(max_length=100)),
                ('event_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomCharityUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254)),
                ('charity_name', models.CharField(blank=True, max_length=255, null=True)),
                ('charity_id', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('charity_address', models.TextField(blank=True, max_length=100, null=True)),
                ('charity_city', models.CharField(blank=True, max_length=20, null=True)),
                ('charity_state', models.CharField(blank=True, max_length=20, null=True)),
                ('charity_zipcode', models.CharField(blank=True, max_length=10, null=True)),
                ('groups', models.ManyToManyField(related_name='charity_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(related_name='charity_user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_token', models.CharField(max_length=100)),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='charity_user.customcharityuser')),
            ],
        ),
    ]
