# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula_formset', '0005_auto_20151023_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ficha_t',
            name='escolhas',
        ),
        migrations.AddField(
            model_name='ficha_t',
            name='radio',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
