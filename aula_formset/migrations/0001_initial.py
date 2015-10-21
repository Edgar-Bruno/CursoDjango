# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ficha_t',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caracteristica', models.CharField(max_length=40, null=True, blank=True)),
                ('informacao', models.CharField(max_length=140, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nave',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name=b'Date Published')),
                ('nave', models.CharField(max_length=20, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='ficha_t',
            name='nave',
            field=models.ForeignKey(to='aula_formset.Nave'),
        ),
    ]
