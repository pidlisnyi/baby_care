# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('care', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='pub_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_text',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='article_title',
            new_name='title',
        ),
    ]