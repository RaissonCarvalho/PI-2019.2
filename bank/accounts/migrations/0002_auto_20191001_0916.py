# Generated by Django 2.2.6 on 2019-10-01 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
