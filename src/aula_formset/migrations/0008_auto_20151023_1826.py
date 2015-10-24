# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula_formset', '0007_auto_20151023_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficha_t',
            name='navenome',
        ),
        migrations.AddField(
            model_name='nave',
            name='navenome',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
