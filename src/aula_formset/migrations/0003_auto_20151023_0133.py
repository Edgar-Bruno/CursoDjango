# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula_formset', '0002_auto_20151023_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha_t',
            name='caracteristica',
            field=models.CharField(default=0, max_length=20, choices=[(0, b'Low'), (1, b'Medium'), (2, b'High')]),
        ),
    ]
