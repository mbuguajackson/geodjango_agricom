from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePageView),
    #load data into our application
    path('county_data/', county_datasets, name='county_datasets'),
    path('incidence_data/', incidents, name='incidents'),
  
]
