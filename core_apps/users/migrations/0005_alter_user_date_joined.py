# Generated by Django 3.2.11 on 2022-11-09 18:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 9, 18, 54, 24, 825501, tzinfo=utc)),
        ),
    ]
