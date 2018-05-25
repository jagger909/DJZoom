# Generated by Django 2.0.5 on 2018-05-07 09:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0018_auto_20180507_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='image',
            field=models.ImageField(default=1, upload_to='imagepool/%Y/%m', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='new',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2018, 5, 7, 12, 12, 50, 673946), verbose_name='Опубликована'),
        ),
    ]
