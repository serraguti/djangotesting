from django.shortcuts import render
from television import models as md

# Create your views here.
def index(request):
    service = md.ServiceSeries()
    informacion = {
        "series": service.getSeries()
    }
    return render(request, "index.html", informacion)