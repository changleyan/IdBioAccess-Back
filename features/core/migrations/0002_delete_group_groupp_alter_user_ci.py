# Generated by Django 4.2.6 on 2023-11-02 16:09

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.CreateModel(
            name='Groupp',
            fields=[
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'db_table': 'tbl_group',
                'permissions': (('list_group', 'Can list groups'),),
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='ci',
            field=models.CharField(max_length=11, null=True, validators=[django.core.validators.RegexValidator(message='El CI de Cuba debe tener 11 dígitos numéricos', regex='^\\d{11}$')]),
        ),
    ]
