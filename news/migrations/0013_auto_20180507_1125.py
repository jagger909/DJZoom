# Generated by Django 2.0.5 on 2018-05-07 08:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0012_auto_20180507_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 5, 7, 11, 25, 6, 325901), verbose_name='Опубликована'),
        ),
    ]
