# Generated by Django 2.2.6 on 2019-10-02 12:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20191002_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 2, 12, 47, 52, 992879, tzinfo=utc)),
        ),
    ]
