from django.db import models
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

class CountryFlag(models.Model):

    country_name = models.CharField(max_length=30,blank=True)
    country_flag_image = models.FileField(upload_to='country_flags', default="some", null=True)
    country_code = models.CharField(max_length=30)
    def __str__(self):
        return self.country_name

class Country(models.Model):

    name = models.CharField(max_length=40,blank=True)
    total_cases = models.IntegerField(default="0")
    new_cases = models.IntegerField(default="0")
    total_death = models.IntegerField(default="0")
    new_death = models.IntegerField(default="0")
    total_recovered = models.IntegerField(blank=True)
    new_recovered = models.IntegerField(default="0")
    active_cases = models.IntegerField(default="0")
    serious_critical = models.IntegerField(default="0")
    total_cases_1m_pop = models.IntegerField(default="0")
    deaths_1m_pop = models.IntegerField(default="0")
    total_test = models.IntegerField(default="0")
    test_1m_pop = models.IntegerField(default="0")
    population = models.IntegerField(default="0")
    date = models.DateTimeField(default="0")

    def __str__(self):
        return self.name

class State(models.Model):
    fips = models.CharField(max_length=40)
    country = models.CharField(max_length=120,blank=True,null=True)
    state = models.CharField(max_length=100,default=None,null=True)
    county = models.CharField(max_length=40,default=None,blank=True,null=True)
    level = models.CharField(max_length=40,default=None,null=True)
    lat = models.CharField(max_length=100,default=None,null=True)
    long = models.CharField(max_length=100,default=None,null=True)
    population = models.IntegerField(blank=True,default=0,null=True)

    metrics_testPositivityRatio = models.FloatField(default=0.00,null=True)
    metrics_caseDensity = models.FloatField(default=0.00,null=True)
    metrics_contactTracerCapacityRatio = models.FloatField(default=0.00,null=True)
    metrics_infectionRate = models.FloatField(default=0.00,null=True)
    metrics_infectionRateCI90 = models.FloatField(default=0.00,null=True)
    metrics_icuHeadroomRatio = models.FloatField(default=0.00,null=True)

    metrics_icuHeadroomDetails_currentIcuCovid = models.IntegerField(default=0,null=True)
    metrics_icuHeadroomDetails_currentIcuCovidMethod = models.CharField(max_length=60,null=True)
    metrics_icuHeadroomDetails_currentIcuNonCovid = models.IntegerField(default=0,null=True)
    metrics_icuHeadroomDetails_currentIcuNonCovidMethod = models.CharField(max_length=60,null=True)

    actuals_cases = models.IntegerField(default=0,null=True)
    actuals_deaths = models.IntegerField(default=0,null=True)
    actuals_positiveTests = models.IntegerField(default=0,null=True)
    actuals_negativeTests = models.IntegerField(default=0,null=True)
    actuals_contactTracers = models.IntegerField(default=0,null=True)
    actuals_hospitalBeds_capacity = models.IntegerField(default=0,blank=True,null=True)
    actuals_hospitalBeds_currentUsageTotal = models.IntegerField(blank=True,null=True)
    actuals_hospitalBeds_currentUsageCovid = models.IntegerField(default=0,blank=True,null=True)
    actuals_hospitalBeds_typicalUsageRate = models.FloatField(default=0.00,blank=True,null=True)

    actuals_icuBeds_capacity = models.IntegerField(default=0,blank=True,null=True)
    actuals_icuBeds_currentUsageTotal = models.IntegerField(default=0,blank=True,null=True)
    actuals_icuBeds_currentUsageCovid = models.IntegerField(default=0,blank=True,null=True)
    actuals_icuBeds_typicalUsageRate = models.IntegerField(default=0,blank=True,null=True)
    lastUpdatedDate = models.CharField(max_length=80,blank=True,null=True)

    def _str_(self):
        return self.state

class CovidRecordUpdateSetting(models.Model):

    days = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(360),
            MinValueValidator(0),
        ])
    hour = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(60),
            MinValueValidator(0),
        ])
    minutes = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(60),
            MinValueValidator(0)
        ])
    seconds = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(60),
            MinValueValidator(0),
        ])

class CovidMobility(models.Model):
    country = models.CharField(max_length=120)
    date = models.CharField(max_length=120,blank=True,null=True)
    retailRecreation = models.IntegerField(default=None,null=True)
    groceryPharmacy = models.CharField(max_length=40,default=None,blank=True,null=True)
    parks = models.CharField(max_length=40,default=None,null=True)
    transitStations = models.CharField(max_length=40,default=None,null=True)
    workplaces = models.CharField(max_length=40,default=None,null=True)
    residential = models.CharField(max_length=40,blank=True,null=True)
    diving = models.CharField(max_length=40,blank=True,null=True)
    transit = models.CharField(max_length=40,blank=True,null=True)
    walking = models.CharField(max_length=40,blank=True,null=True)

    def _str_(self):
        return self.country

class CovidVaccin(models.Model):
    status = models.CharField(max_length=120)
    stage1 = models.CharField(max_length=120,blank=True,null=True)
    stage2 = models.CharField(max_length=40,default=None,null=True)
    s3Phase1 = models.CharField(max_length=40,default=None,blank=True,null=True)
    s3Phase2 = models.CharField(max_length=40,default=None,null=True)
    s3Phase3 = models.CharField(max_length=40,default=None,null=True)
    stage4 = models.CharField(max_length=40,default=None,null=True)
    stage5 = models.CharField(max_length=40,blank=True,null=True)
    def _str_(self):
        return self.status
