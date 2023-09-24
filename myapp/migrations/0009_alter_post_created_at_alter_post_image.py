# Generated by Django 4.0.3 on 2022-06-04 12:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_post_created_at_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 17, 48, 13, 536683)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='nophoto.png', upload_to='post_images'),
        ),
    ]
