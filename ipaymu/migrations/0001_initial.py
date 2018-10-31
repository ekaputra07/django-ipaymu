# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IpaymuSessionID',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sessid', models.TextField(verbose_name='Session ID', db_index=True)),
                ('verified', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='verified')),
            ],
            options={
                'db_table': 'ipaymu_sessid',
                'verbose_name': 'Ipaymu Session',
                'verbose_name_plural': 'Ipaymu Sessions',
            },
        ),
    ]
