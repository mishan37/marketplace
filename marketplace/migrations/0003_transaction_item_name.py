# Generated by Django 2.0.2 on 2018-04-09 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20180409_0241'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='item_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
