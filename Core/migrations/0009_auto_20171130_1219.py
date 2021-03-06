# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_auto_20171116_1500'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='FS_URL',
            new_name='F5_URL',
        ),
        migrations.AddField(
            model_name='customer',
            name='Control_M_Template',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='Customer_DL',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='P_and_P_Link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='SLA',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='SSO',
            field=models.CharField(choices=[('-', '-'), ('yes', 'Yes'), ('no', 'No')], default='-', max_length=10),
        ),
        migrations.AddField(
            model_name='customer',
            name='SSO_URL',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='SharePoint_Link',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Server_Type',
            field=models.CharField(choices=[('-', '-'), ('physical', 'Physical'), ('vm', 'VM'), ('lpar', 'LPAR')], default='-', max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Status',
            field=models.CharField(choices=[('Steady', 'Steady'), ('Transition', 'Transitoion'), ('Decomm', 'Decomm')], max_length=1000, null=True),
        ),
    ]
