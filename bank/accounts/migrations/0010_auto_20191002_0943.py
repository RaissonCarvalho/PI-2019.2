# Generated by Django 2.2.6 on 2019-10-02 12:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20191002_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='creation_date',
            field=models.DateField(auto_created=True, default=datetime.datetime(2019, 10, 2, 12, 43, 25, 804948, tzinfo=utc)),
        ),
    ]
