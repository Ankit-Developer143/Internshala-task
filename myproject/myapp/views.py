from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.contrib import messages
from .models import Data
from django.contrib.auth.forms import UserCreationForm
from .forms import DataForm

# Create your views here.
def home(request):
    
    
    return render(request,'myapp/index.html')


def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username,password = password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,'Succefully Login !!')
            return redirect('home')
        else:
            messages.info(request,"invalid credintial")
        return redirect('login')
    return render(request,'myapp/login.html')
def logout(request):
    auth.logout(request)
    return redirect('home')
    
    
    
    
    
    
def registration(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request,'Username already exists !!')
                return redirect('registration')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'email already exists !!')
            else:
                user = User.objects.create_user(username=username, password=password1,email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,"Created succefully !!")
                return redirect('login')
        else:
             messages.info(request,'password not match')
             return redirect('registration')
    return render(request,'myapp/signup.html')


def createreport(request):
  form  = DataForm()
  if request.method == 'POST':
    form = DataForm(request.POST)
    if form.is_valid():
      # save the form into database
      form.save()
      return redirect('createreport')
  
  return render(request,'myapp/report.html',{'form':form})