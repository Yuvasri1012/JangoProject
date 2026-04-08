from django.shortcuts import render,redirect
from .models import DressInfo
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.

def about_page(request):
    return render(request,"about.html")

def get_all_data(request):
    products = DressInfo.objects.all()
    return render(request,'shop.html',{"products":products})

def signup_page(request):
    return render(request,'signup.html')

def login_page(request):
    return render(request,'login.html')

def signup_action(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
         
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                return redirect('signup')
            else:
                user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,email=email,password=password)
                user.save()
                return redirect('homepage')       
        else:
            return redirect('signup')   
        
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        
        if user is not None:
            print("Success")
            login(request,user)
            return redirect('homepage')
        else:
            print("Fail")
            return redirect('login')
        
    messages.error(request, "Invalid username or password")
    return redirect('login')
        
        