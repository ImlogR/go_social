# Generated by Django 4.0.3 on 2022-06-02 09:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_post_profile_pic_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 2, 14, 47, 41, 695677)),
        ),
        migrations.AlterField(
            model_name='post',
            name='profile_pic',
            field=models.ImageField(default='LionMask_2.jpg', upload_to='profile_images'),
        ),
    ]
