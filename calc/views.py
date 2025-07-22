from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view




# Create your views here.
def home(request):
    return render(request,'home.html',{'name':'ejaz'})

@api_view(['GET'])
def home1(request):
    person={'name':'ejaz'}
    return Response(person)

def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    
    return render(request, 'result.html', {'result':res})

@api_view(['POST'])
def add1(request):
    val1=int(request.data.get('num1'))
    val2=int(request.data.get('num2'))
    res=val1+val2
    result={'res':res}
    return Response(result)
