# Generated by Django 3.1.2 on 2020-10-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_auto_20201010_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='actuals_cases',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='actuals_contactTracers',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='actuals_deaths',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='actuals_icuBeds_capacity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='actuals_negativeTests',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='actuals_positiveTests',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='country',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='lat',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='level',
            field=models.CharField(default=None, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='long',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='metrics_caseDensity',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='metrics_contactTracerCapacityRatio',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='metrics_icuHeadroomDetails_currentIcuCovid',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='metrics_icuHeadroomDetails_currentIcuCovidMethod',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='metrics_icuHeadroomDetails_currentIcuNonCovid',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='metrics_icuHeadroomDetails_currentIcuNonCovidMethod',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='metrics_icuHeadroomRatio',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='metrics_infectionRate',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='metrics_infectionRateCI90',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='metrics_testPositivityRatio',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='population',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='state',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
    ]
