from django.shortcuts import render,HttpResponse
from .models import Counties
from django.core.serializers import serialize


# Create your views here.
def HomePageView(request):
    
    return render(request, "reporter/home_page.html")

def county_datasets(request):
    counties= serialize('geojson',Counties.objects.all())
    return HttpResponse(counties, content_type='json')

    