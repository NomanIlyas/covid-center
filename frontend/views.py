from datetime import datetime
from django.utils import timezone
from django.shortcuts import render
import covid_daily
from frontend.models import Country


def importCountries():
    overview = covid_daily.overview(as_json=True)
    # data = covid_daily.data(country='spain', chart='total-currently-infected-linear', as_json=False)
    # print(data.head())
    country = Country.objects.all()
    for key in overview:
        if country:
            country.name = key.get('Country,Other', None)
            country.total_cases = key.get('TotalCases', None)
            country.new_cases = key.get('NewCases', None)
            country.total_death = key.get('TotalDeaths', None)
            country.new_death = key.get('NewDeaths', None)
            country.total_recovered = key.get('TotalRecovered', None)
            country.new_recovered = key.get('NewRecovered', None)
            country.active_cases = key.get('ActiveCases', None)
            country.serious_critical = key.get('Serious,Critical', None)
            country.total_cases_1m_pop = key.get('TotCases/1M pop', None)
            country.deaths_1m_pop = key.get('Deaths/1M pop', None)
            country.total_test = key.get('TotalTests', None)
            country.test_1m_pop = key.get('Tests/1M pop', None)
            country.population = key.get('Population', None)
            country.date = datetime.today()
            # covid_record= Country.objects.create(country_code=country_code,total_cases=total_cases,date=date)
            Country.objects.filter(name=country.name).update(name=country.name, total_cases=country.total_cases,
                                                             new_cases=country.new_cases,
                                                             new_recovered=country.new_recovered,
                                                             total_death=country.total_death,
                                                             new_death=country.new_death,
                                                             total_recovered=country.total_recovered,
                                                             active_cases=country.active_cases,
                                                             serious_critical=country.serious_critical,
                                                             total_cases_1m_pop=country.total_cases_1m_pop,
                                                             deaths_1m_pop=country.deaths_1m_pop,
                                                             total_test=country.total_test,
                                                             test_1m_pop=country.test_1m_pop,
                                                             population=country.population, date=country.date)
        else:
            name = key.get('Country,Other', None)
            total_cases = key.get('TotalCases', None)
            new_cases = key.get('NewCases', None)
            total_death = key.get('TotalDeaths', None)
            new_death = key.get('NewDeaths', None)
            total_recovered = key.get('TotalRecovered', None)
            new_recovered = key.get('NewRecovered', None)
            active_cases = key.get('ActiveCases', None)
            serious_critical = key.get('Serious,Critical', None)
            total_cases_1m_pop = key.get('TotCases/1M pop', None)
            deaths_1m_pop = key.get('Deaths/1M pop', None)
            total_test = key.get('TotalTests', None)
            test_1m_pop = key.get('Tests/1M pop', None)
            population = key.get('Population', None)
            date = datetime.today()
            covid_record = Country.objects.create(name=name, total_cases=total_cases, new_cases=new_cases,
                                                  new_recovered=new_recovered, total_death=total_death,
                                                  new_death=new_death, total_recovered=total_recovered,
                                                  active_cases=active_cases, serious_critical=serious_critical,
                                                  total_cases_1m_pop=total_cases_1m_pop, deaths_1m_pop=deaths_1m_pop,
                                                  total_test=total_test, test_1m_pop=test_1m_pop, population=population,
                                                  date=date)
            covid_record.save()
    return timezone.now().strftime('%X')
