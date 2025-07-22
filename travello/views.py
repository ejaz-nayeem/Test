from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

#Destination2, Destination3
# Create your views here.
def index(request):
    
    descs=Destination.objects.all()
    
    return render(request, 'index.html', {'descs':descs})

@api_view(['GET'])
def index1(request):
    
    descs=Destination.objects.all()
    serializer=DestinationSerializer(descs, many=True)
    return Response(serializer.data)