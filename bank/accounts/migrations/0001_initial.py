# Generated by Django 2.2.6 on 2019-10-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('owner', models.CharField(max_length=40)),
                ('balance', models.FloatField()),
            ],
        ),
    ]
