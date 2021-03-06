# Generated by Django 3.1.2 on 2020-10-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0008_auto_20201010_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='actuals_icuBeds_currentUsageCovid',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='actuals_icuBeds_currentUsageTotal',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='actuals_icuBeds_typicalUsageRate',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='lastUpdatedDate',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
