# Generated by Django 4.0.3 on 2022-06-04 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_alter_post_created_at_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 6, 4, 17, 52, 56, 584037)),
        ),
    ]
