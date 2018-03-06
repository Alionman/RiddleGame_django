# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_telephone_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='telephone',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
