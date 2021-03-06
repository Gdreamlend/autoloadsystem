# Generated by Django 2.1.7 on 2019-04-08 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='slide',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='slide',
            name='status',
            field=models.CharField(default=0, max_length=2),
        ),
        migrations.AlterField(
            model_name='slide',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
