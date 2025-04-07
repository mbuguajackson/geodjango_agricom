from django.contrib import admin
from django.urls import path

from .views import HomePageView

urlpatterns = [
    path('', HomePageView),
    path('county_data$', HomePageView),
    path('incidents$')
]
