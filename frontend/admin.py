from django.contrib import admin
from .models import Country,CountryFlag,State

admin.site.site_header = "The Covid Center Admin Panel"
admin.site.site_title = "The Covid Center"
admin.site.index_title = "The Covid Center"


class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', "total_cases", "new_cases", "total_death", "new_death", "total_recovered", "active_cases", "serious_critical", "total_cases_1m_pop", "deaths_1m_pop", "total_test", "test_1m_pop", "population", "date")
    search_fields = ('name', "total_cases", "new_cases", "total_death", )
    list_max_show_all = 25
    ordering = ['pk']
    list_filter = ("name",)
    list_display_links = ['name']



admin.site.register(Country,CountryAdmin)


class CountryFlagAdmin(admin.ModelAdmin):

    list_display = ('id', 'country_name', 'country_flag_image', 'country_code', )
    list_max_show_all = 25
    ordering = ['pk']
    list_filter = ("country_name",)


admin.site.register(CountryFlag, CountryFlagAdmin)

#
class StateAdmin(admin.ModelAdmin):

    list_display = ('id', 'fips', 'country', 'state', 'population',
                    'metrics_testPositivityRatio', 'metrics_caseDensity', 'metrics_contactTracerCapacityRatio',
                    'metrics_infectionRate', 'metrics_infectionRateCI90', 'metrics_icuHeadroomRatio',
                    'metrics_icuHeadroomDetails_currentIcuCovid',
                    'metrics_icuHeadroomDetails_currentIcuNonCovid',
                    'actuals_cases', 'actuals_deaths','actuals_positiveTests', 'actuals_negativeTests','actuals_contactTracers',
                    'actuals_hospitalBeds_capacity','actuals_hospitalBeds_currentUsageCovid',
                    'actuals_hospitalBeds_typicalUsageRate','actuals_icuBeds_capacity',
                    'actuals_icuBeds_currentUsageCovid', 'lastUpdatedDate',)
    list_max_show_all = 25
    ordering = ['pk']
    list_filter = ['state']
    search_fields = ('country', 'state',)

admin.site.register(State, StateAdmin)
