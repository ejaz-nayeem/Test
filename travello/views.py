from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination
#Destination2, Destination3
# Create your views here.
def index(request):
    
    desc1=Destination()
    desc1.name='dhaka'
    desc1.description='dhakadddddddddd'
    desc1.price=1
    desc1.image='destination_1.jpg'
    desc1.offer=False 
    
    desc2=Destination()
    desc2.name='CTG'
    desc2.description='ctggggggg'
    desc2.price=2
    desc2.image='destination_2.jpg'
    desc2.offer=True
    
    desc3=Destination()
    desc3.name='Mymen'
    desc3.description='myyymmmmmm'
    desc3.price=3
    desc3.image='destination_3.jpg'
    desc3.offer=False
    
    descs=[desc1, desc2, desc3]
    
    return render(request, 'index.html', {'descs':descs})