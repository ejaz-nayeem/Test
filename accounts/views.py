from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def register(request):
    
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user name exists")
                return redirect('register')
                
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email exists")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,first_name=first_name,last_name=last_name,password=password1)
                user.save()
                print("user created")
                return redirect('login')
                
                
             
        else:
            messages.info(request,"password mismatch")
            return redirect('register') 
        return redirect('/')
            
          
    else:
        
        return render(request, 'register.html')
    



def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,"invalid info")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def rajshahi(request):
    if request.user.is_authenticated:
        
        return render(request, "rajshahi.html")
    else:
        return redirect('login')

from rest_framework import status
@api_view(['POST'])    
def register1(request):
    
    if request.method=="POST":
        first_name=request.data.get('first_name')
        last_name=request.data.get('last_name')
        username=request.data.get('username')
        password1=request.data.get('password1')
        password2=request.data.get('password2')
        email=request.data.get('email')
        if not all([username, password, password2, email]):
            
            return Response({'error': 'Username, password, and email are required.'}, status=status.HTTP_400_BAD_REQUEST)

    if password != password2:
        
        return Response(
            {'error': 'Passwords do not match'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'Username already exists'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(email=email).exists():
        return Response(
            {'error': 'Email already registered'}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    # --- End of Validation ---

    # If all checks pass, create the user
    user = User.objects.create_user(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password
    )
    
    
    return Response(
        {'message': 'User created successfully'}, 
        status=status.HTTP_201_CREATED
    )
 
def login1(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response(
            {'error': 'Please provide both username and password'},
            status=status.HTTP_400_BAD_REQUEST
        )

   
    user = authenticate(username=username, password=password)

    if user is not None:
        
        login(request, user)
        
      
        return Response(
            {'message': f'Welcome {username}! Login successful.'},
            status=status.HTTP_200_OK
        )
    else:
     
        return Response(
            {'error': 'Invalid Credentials'},
            status=status.HTTP_401_UNAUTHORIZED 
        )

@api_view(['POST'])    
def logout1(request):
    auth.logout(request)
    return Response(
        {'detail': 'Successfully logged out.'}, 
        status=status.HTTP_200_OK
    )
@api_view(['POST'])
def rajshahi1(request):
    data = {
        'message': f'Hello, {request.user.username}! You are seeing protected data.',
        'location': 'Rajshahi',
        'attractions':'Padma Garden',
            }
    
   
    return Response(data, status=status.HTTP_200_OK)