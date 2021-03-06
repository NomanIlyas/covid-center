# Generated by Django 2.2.5 on 2020-10-15 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0014_covidmobility'),
    ]

    operations = [
        migrations.CreateModel(
            name='CovidVaccin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=120)),
                ('stage1', models.CharField(blank=True, max_length=120, null=True)),
                ('stage2', models.CharField(default=None, max_length=40, null=True)),
                ('s3Phase1', models.CharField(blank=True, default=None, max_length=40, null=True)),
                ('s3Phase2', models.CharField(default=None, max_length=40, null=True)),
                ('s3Phase3', models.CharField(default=None, max_length=40, null=True)),
                ('stage4', models.CharField(default=None, max_length=40, null=True)),
                ('stage5', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
    ]
