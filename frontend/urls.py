from django.urls import path
from django.conf.urls import url
from . import views
app_name="c19"
urlpatterns = [
    path('', views.index,name="index" ),
    path('world/', views.world,name="world" ),
    path('blogs', views.blogs,name="blogs" ),
    path('news/', views.news,name="news" ),
    # url(r'^world/(?P<name>[a-z]+)/$', views.country,name="world" ),
    url(r'^country/(?P<name>[0-9]+)/$', views.country,name="country" ),
    path('united_states/', views.united_states,name="united_states"),
    path('importStates/', views.importStates ),
    path('importCountries/', views.importCountries ),
]