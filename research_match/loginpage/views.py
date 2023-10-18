from imaplib import _Authenticator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    
    return render(request, "registration/loginpage.html")

def signup(request):

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(email, password)
        myuser.first_name = firstname
        myuser.last_name = lastname

        myuser.save()

        messages.success(request,"Your Account has been successfully created.")

        return redirect('studentlogin')



    return render(request, "registration/loginpage.html")

def studentlogin(request):


    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "registration/profile.html", {'firstname': firstname})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')


    return render(request, "registration/loginpage.html")

def signout(request):
    pass