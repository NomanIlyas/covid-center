from datetime import datetime
from django.utils import timezone
from django.http import HttpResponse
from django.shortcuts import render
import covid_daily
import requests
from frontend.models import Country, State
import json
import itertools

def importStates():
    url = "https://api.covidactnow.org/v2/states.json?apiKey="
    apiKey = "3d6a9e2ce7af4fa39b3ee24f0d6074a3"
    objects = requests.get(url + apiKey).content
    data = json.loads(objects)

    states = State.objects.all()

    for key in data:
        fips = key.get('fips', None)
        country = key.get('country', None)
        state = key.get('state', None)
        county = key.get('county', None)
        level = key.get('level', None)
        lat = key.get('lat', None)
        long = key.get('long', None)
        population = key.get('population', None)

        metrics = key.get('metrics', None)
        metrics_testPositivityRatio = metrics.get('testPositivityRatio', None)
        metrics_caseDensity = metrics.get('caseDensity', None)
        metrics_contactTracerCapacityRatio = metrics.get('contactTracerCapacityRatio', None)
        metrics_infectionRate = metrics.get('infectionRate', None)
        metrics_infectionRateCI90 = metrics.get('infectionRateCI90', None)
        metrics_icuHeadroomRatio = metrics.get('icuHeadroomRatio', None)
        metrics_icuHeadroomDetails = metrics.get('icuHeadroomDetails', None)

        if metrics_icuHeadroomDetails:
            metrics_icuHeadroomDetails_currentIcuCovid = metrics_icuHeadroomDetails.get('currentIcuCovid', None)
            metrics_icuHeadroomDetails_currentIcuCovidMethod = metrics_icuHeadroomDetails.get('currentIcuCovidMethod', None)
            metrics_icuHeadroomDetails_currentIcuNonCovid = metrics_icuHeadroomDetails.get('currentIcuNonCovid', None)
            metrics_icuHeadroomDetails_currentIcuNonCovidMethod = metrics_icuHeadroomDetails.get('currentIcuNonCovidMethod', None)

        else:
            metrics_icuHeadroomDetails_currentIcuCovid = 0
            metrics_icuHeadroomDetails_currentIcuCovidMethod = 0
            metrics_icuHeadroomDetails_currentIcuNonCovid = 0
            metrics_icuHeadroomDetails_currentIcuNonCovidMethod = 0

        actuals = key.get('actuals', None)
        actuals_cases = actuals.get('cases', None)
        actuals_deaths = actuals.get('deaths', None)
        actuals_positiveTests = actuals.get('positiveTests', None)
        actuals_negativeTests = actuals.get('negativeTests', None)
        actuals_contactTracers = actuals.get('contactTracers', None)

        hospitalBeds = actuals.get('hospitalBeds', None)
        actuals_hospitalBeds_capacity = hospitalBeds.get('capacity', None)
        actuals_hospitalBeds_currentUsageTotal = hospitalBeds.get('currentUsageTotal', None)
        actuals_hospitalBeds_currentUsageCovid = hospitalBeds.get('currentUsageCovid', None)
        actuals_hospitalBeds_typicalUsageRate = hospitalBeds.get('typicalUsageRate', None)

        actuals_icuBeds = actuals.get('icuBeds', None)
        actuals_icuBeds_capacity = actuals_icuBeds.get('capacity', None)
        actuals_icuBeds_currentUsageTotal = actuals_icuBeds.get('currentUsageTotal', None)
        actuals_icuBeds_currentUsageCovid = actuals_icuBeds.get('currentUsageCovid', None)
        actuals_icuBeds_typicalUsageRate = actuals_icuBeds.get('typicalUsageRate', None)
        # lastUpdatedDate = key.get('lastUpdatedDate', None)

        if states:

            State.objects.filter(state=state).update(fips=fips, country=country, county=county, level=level,
                                 lat=lat, long=long, population=population,
                                 metrics_testPositivityRatio=metrics_testPositivityRatio,
                                 metrics_caseDensity=metrics_caseDensity,
                                 metrics_contactTracerCapacityRatio=metrics_contactTracerCapacityRatio,
                                 metrics_infectionRate=metrics_infectionRate,
                                 metrics_infectionRateCI90=metrics_infectionRateCI90,
                                 metrics_icuHeadroomRatio=metrics_icuHeadroomRatio,
                                 metrics_icuHeadroomDetails_currentIcuCovid=metrics_icuHeadroomDetails_currentIcuCovid,
                                 metrics_icuHeadroomDetails_currentIcuCovidMethod=metrics_icuHeadroomDetails_currentIcuCovidMethod,
                                 metrics_icuHeadroomDetails_currentIcuNonCovid=metrics_icuHeadroomDetails_currentIcuNonCovid,
                                 metrics_icuHeadroomDetails_currentIcuNonCovidMethod=metrics_icuHeadroomDetails_currentIcuNonCovidMethod,
                                 actuals_cases=actuals_cases,
                                 actuals_hospitalBeds_capacity=actuals_hospitalBeds_capacity,
                                 actuals_deaths=actuals_deaths,
                                 actuals_positiveTests=actuals_positiveTests,
                                 actuals_negativeTests=actuals_negativeTests,
                                 actuals_contactTracers=actuals_contactTracers,
                                 actuals_hospitalBeds_currentUsageTotal=actuals_hospitalBeds_currentUsageTotal,
                                 actuals_hospitalBeds_currentUsageCovid=actuals_hospitalBeds_currentUsageCovid,
                                 actuals_hospitalBeds_typicalUsageRate=actuals_hospitalBeds_typicalUsageRate,
                                 actuals_icuBeds_capacity=actuals_icuBeds_capacity,
                                 actuals_icuBeds_currentUsageTotal=actuals_icuBeds_currentUsageTotal,
                                 actuals_icuBeds_currentUsageCovid=actuals_icuBeds_currentUsageCovid,
                                 actuals_icuBeds_typicalUsageRate=actuals_icuBeds_typicalUsageRate,
                                 lastUpdatedDate=datetime.today())
        else:
            covid_states = State.objects.create(fips=fips, country=country, state=state, county=county, level=level,
                                 lat=lat, long=long, population=population,
                                 metrics_testPositivityRatio=metrics_testPositivityRatio,
                                 metrics_caseDensity=metrics_caseDensity,
                                 metrics_contactTracerCapacityRatio=metrics_contactTracerCapacityRatio,
                                 metrics_infectionRate=metrics_infectionRate,
                                 metrics_infectionRateCI90=metrics_infectionRateCI90,
                                 metrics_icuHeadroomRatio=metrics_icuHeadroomRatio,
                                 metrics_icuHeadroomDetails_currentIcuCovid=metrics_icuHeadroomDetails_currentIcuCovid,
                                 metrics_icuHeadroomDetails_currentIcuCovidMethod=metrics_icuHeadroomDetails_currentIcuCovidMethod,
                                 metrics_icuHeadroomDetails_currentIcuNonCovid=metrics_icuHeadroomDetails_currentIcuNonCovid,
                                 metrics_icuHeadroomDetails_currentIcuNonCovidMethod=metrics_icuHeadroomDetails_currentIcuNonCovidMethod,
                                 actuals_cases=actuals_cases,
                                 actuals_hospitalBeds_capacity=actuals_hospitalBeds_capacity,
                                 actuals_deaths=actuals_deaths,
                                 actuals_positiveTests=actuals_positiveTests,
                                 actuals_negativeTests=actuals_negativeTests,
                                 actuals_contactTracers=actuals_contactTracers,
                                 actuals_hospitalBeds_currentUsageTotal=actuals_hospitalBeds_currentUsageTotal,
                                 actuals_hospitalBeds_currentUsageCovid=actuals_hospitalBeds_currentUsageCovid,
                                 actuals_hospitalBeds_typicalUsageRate=actuals_hospitalBeds_typicalUsageRate,
                                 actuals_icuBeds_capacity=actuals_icuBeds_capacity,
                                 actuals_icuBeds_currentUsageTotal=actuals_icuBeds_currentUsageTotal,
                                 actuals_icuBeds_currentUsageCovid=actuals_icuBeds_currentUsageCovid,
                                 actuals_icuBeds_typicalUsageRate=actuals_icuBeds_typicalUsageRate,
                                 lastUpdatedDate=datetime.today())
            covid_states.save()

    return timezone.now().strftime('%X')




def importCountries():
    overview = covid_daily.overview(as_json=True)
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
