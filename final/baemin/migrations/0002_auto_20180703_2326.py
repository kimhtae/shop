# Generated by Django 2.0.7 on 2018-07-03 14:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('baemin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ('-id',)},
        ),
        migrations.AddField(
            model_name='shop',
            name='name_kr',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
