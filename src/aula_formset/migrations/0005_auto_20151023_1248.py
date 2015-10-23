# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aula_formset', '0004_auto_20151023_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ficha_t',
            old_name='escolha',
            new_name='escolhas',
        ),
    ]
