# Generated by Django 2.0.7 on 2018-07-03 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baemin', '0002_auto_20180703_2326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='name_kr',
        ),
    ]
