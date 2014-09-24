# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20140919_2005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='category_id',
            new_name='category',
        ),
    ]
