from django.db import models

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

# Create your models here.


class State(models.Model):
    c_id = models.ForeignKey('Country',on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=40,blank=True)

    def __str__(self):
        return self.name

# Create your models here.


class Province(models.Model):
    s_id = models.ForeignKey('State', on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=40,blank=True)
    def __str__(self):
        return self.name

# Create your models here.
