# Generated by Django 2.0.5 on 2018-05-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=123, upload_to='categories/list', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
