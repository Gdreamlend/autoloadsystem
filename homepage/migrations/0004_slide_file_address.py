# Generated by Django 2.1.7 on 2019-04-08 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20190408_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='file_address',
            field=models.CharField(default='', max_length=2000),
        ),
    ]