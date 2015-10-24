# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula_formset', '0006_auto_20151023_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha_t',
            name='navenome',
            field=models.CharField(max_length=140, null=True),
        ),
        migrations.AlterField(
            model_name='ficha_t',
            name='caracteristica',
            field=models.CharField(default=0, max_length=20, choices=[(b'Low', b'Low'), (b'Medium', b'Medium'), (b'High', b'High')]),
        ),
    ]
