from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
#Destination2, Destination3
# Create your views here.
def index(request):
    
    descs=Destination.objects.all()
    
    
    return render(request, 'index.html', {'descs':descs})