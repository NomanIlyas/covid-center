# Generated by Django 2.2.5 on 2020-10-20 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0016_auto_20201020_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covidmobility',
            name='retailRecreation',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
