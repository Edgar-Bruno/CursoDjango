# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula_formset', '0003_auto_20151023_0133'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha_t',
            name='escolha',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ficha_t',
            name='caracteristica',
            field=models.CharField(default=0, max_length=20, choices=[(b'XXX', b'Low'), (b'YYY', b'Medium'), (b'ZZZ', b'High')]),
        ),
    ]
