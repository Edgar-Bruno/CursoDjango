# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula_formset', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ficha_t',
            name='caracteristica',
            field=models.IntegerField(default=0, choices=[(0, b'Low'), (1, b'Medium'), (2, b'High')]),
        ),
    ]
