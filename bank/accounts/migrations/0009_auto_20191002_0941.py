# Generated by Django 2.2.6 on 2019-10-02 12:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_account_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2019, 10, 2, 12, 41, 17, 423005, tzinfo=utc)),
        ),
    ]