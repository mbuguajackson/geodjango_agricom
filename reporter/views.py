from django.shortcuts import render
from .models import Counties
from django.core.serializers import serialize


# Create your views here.
def HomePageView(request):
    counties= serialize('geojson',Counties.objects.all())
    return render(request, "reporter/home_page.html", {"counties": counties})


    