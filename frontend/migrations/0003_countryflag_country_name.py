# Generated by Django 3.1 on 2020-10-10 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_auto_20201010_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='countryflag',
            name='country_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
