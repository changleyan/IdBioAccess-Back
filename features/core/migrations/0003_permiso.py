# Generated by Django 4.2.6 on 2023-11-05 15:06

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0002_delete_group_groupp_alter_user_ci'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
            ],
            options={
                'permissions': (('list_permiso', 'Puede listar permisos'),),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.permission',),
            managers=[
                ('objects', django.contrib.auth.models.PermissionManager()),
            ],
        ),
    ]
