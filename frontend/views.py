from datetime import datetime
from django.db.models import Sum, Avg
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import covid_daily
import requests
from django.db.models import Q
from frontend.models import Country, State, CovidVaccin, CovidMobility
import json
import itertools
from django.core import serializers
from django.db import connection
import dictfier
import os
import csv
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials


def vaccinecounts(request):
    url = 'template/VaccineCounts.csv'
    with open(url, 'r') as file:
        data = csv.reader(file)
        count = 0
        for key in data:
            status = key[0]
            stage1 = key[1]
            stage2 = key[2]
            s3Phase1 = key[3]
            s3Phase2 = key[4]
            s3Phase3 = key[5]
            stage4 = key[6]
            stage5 = key[7]
            mobilitydata = CovidVaccin.objects.create(status=status, stage1=stage1,
                                                        stage2=stage2,
                                                        s3Phase1=s3Phase1, s3Phase2=s3Phase2,
                                                        s3Phase3=s3Phase3, stage4=stage4,
                                                        stage5=stage5)
            mobilitydata.save()
    return HttpResponse("test")

def google_sheet(request):
    url = 'template/MobilityData.csv'
    with open(url, 'r') as file:
        data = csv.reader(file)
        count = 0
        for key in data:
            country = key[0]
            date = key[1]
            retailRecreation = key[2]
            groceryPharmacy = key[3]
            parks = key[4]
            transitStations = key[5]
            workplaces = key[6]
            residential = key[7]
            diving = key[8]
            transit = key[9]
            walking = key[10]
            mobilitydata = CovidMobility.objects.create(country=country,date=date,
                                                        retailRecreation=retailRecreation,
                                                        groceryPharmacy=groceryPharmacy,
                                                        parks=parks,transitStations=transitStations,
                                                        workplaces=workplaces,residential=residential,
                                                        diving=diving,transit=transit,walking=walking)
            mobilitydata.save()
    return HttpResponse("test")


def index(requests):
    data = []
    state_records = State.objects.all()
    updated_date = State.objects.get(pk=54)
    print("\t======================\t",updated_date.lastUpdatedDate)
    world = Country.objects.all()
    cursor = connection.cursor()
    cursor.execute('SELECT sum(total_cases) from frontend_country')
    total_world_cases = cursor.fetchone()[0]
    cursor.execute('SELECT sum(active_cases) from frontend_country')
    mild_cases = cursor.fetchone()[0]
    cursor.execute('SELECT sum(serious_critical) from frontend_country')
    serious_critical = cursor.fetchone()[0]
    cursor.execute('SELECT sum(total_recovered) from frontend_country')
    total_recovered = cursor.fetchone()[0]
    cursor.execute('SELECT sum(total_death) from frontend_country')
    total_death = cursor.fetchone()[0]
    closed_cases = total_world_cases - mild_cases

    data = ['{:,}'.format(total_world_cases), '{:,}'.format(mild_cases), '{:,}'.format(serious_critical), '{:,}'.format(closed_cases), '{:,}'.format(total_recovered), '{:,}'.format(total_death)]

    ongoing = CovidVaccin.objects.get(status="Ongoing")
    success = CovidVaccin.objects.get(status="Success")
    print(ongoing.stage1)

    context = {
        'state_records':state_records,
        'updated_date':updated_date,
        'world':world,
        'data':data,
        'success':success,
        'ongoing':ongoing,
    }
    return render(requests,'index.html', context)

def country(requests,name):
    print(str(name))

    country_records = Country.objects.get(pk=name)
    print("\t======================\t", country_records.new_cases)
    context = {
        'country_records':country_records,
    }
    return render(requests,'country.html',context)


def world(requests):

    world = Country.objects.all()
    context = {
        'world':world
    }
    return render(requests,'world.html',context)


def blogs(requests):
    return render(requests,'blogs.html')


def news(requests):
    return render(requests,'news.html')


def united_states(requests):

    updated_date = Country.objects.get(name='USA')
    updated_state = State.objects.all().aggregate(Sum('actuals_hospitalBeds_currentUsageTotal'))
    print("=========================================================",updated_state)
    data = ['{:,}'.format(updated_date.total_cases), '{:,}'.format(updated_date.total_cases), '{:,}'.format(updated_date.new_cases),'{:,}'.format(updated_date.total_death), '{:,}'.format(updated_date.total_cases), '{:,}'.format(updated_date.total_cases)]

    print("==================================",updated_date.name)

    cursor = connection.cursor()
    # plot chart record
    # states FED Balance Sheet

    retail_recreation_data = []
    retail_recreation_labels = []
    queryset = CovidMobility.objects.values('date','retailRecreation')[:5]
    print(str(len(queryset)))
    for entry in queryset:
        retail_recreation_labels.append(entry['date'])
        retail_recreation_data.append(entry['retailRecreation'])
    # return JsonResponse(data={
    #     'retail_recreation_labels': retail_recreation_labels,
    #     'retail_recreation_data': retail_recreation_data,
    # })
    # updated_state = cursor.execute("SELECT ")
    retailrecreation = cursor.execute('SELECT retailRecreation from frontend_covidmobility where country = "United States"')

    cur = connection.cursor()
    dateofretails = cur.execute('SELECT date from frontend_covidmobility where country = "United States" ')
    resident = connection.cursor()
    us_covismobility_record = CovidMobility.objects.filter(Q(country='United States'))
    resid =[]
    grocery =[]
    park =[]
    transit =[]
    work_place =[]
    data = []
    label = []
    # ============== convert to list to plot graph =========== #
    # work_place
    for work in us_covismobility_record:
        work_place.append(work.workplaces)

    # transitStations
    for trans in us_covismobility_record:
        transit.append(trans.transitStations)
    # parks

    for prk in us_covismobility_record:
        park.append(prk.parks)

    # grocerypharmacy
    for groc in us_covismobility_record:
        grocery.append(groc.groceryPharmacy)

    # resident
    for resi in us_covismobility_record:
        resid.append(resi.residential)


    for entry in dateofretails:
        result = list(entry)
        label.append(result)

    for ent in retailrecreation:
        res = list(ent)
        data.append(res)
    #     key indicator graph ploting
    state_record = State.objects.all()
    for a in state_record:
        print(a)
    # states_record = State.objects.filter(Q('lastUpdatedDate')).annotate()

    return render(requests,'united-states.html', {'updated_date': updated_date,
                                                  'data': data,'label': label,
                                                  'updated_state': updated_state,
                                                  'retail_recreation_labels': retail_recreation_labels,
                                                  'retail_recreation_data': retail_recreation_data,
                                                  'resid': resid,
                                                  'grocery': grocery,
                                                  'park': park,
                                                  'transit': transit,
                                                  'work_place': work_place,

                                                  })

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
