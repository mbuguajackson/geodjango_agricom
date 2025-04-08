from django.shortcuts import render,HttpResponse
from .models import Counties, Incidence
from django.core.serializers import serialize
from django.views.generic import TemplateView

#create views
class HomePageView(TemplateView):
    template_name='index.html'

def county_datasets(request):
    counties= serialize('geojson', Counties.objects.all())
    return HttpResponse(counties,content_type='json')

def incidents(request):
    incidence= serialize('geojson', Incidence.objects.all())
    return HttpResponse(incidence,content_type='json')