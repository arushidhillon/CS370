
from email.message import EmailMessage
import django
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import admin
from django.urls import path, include, reverse
from . import views
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from research_match import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_str, force_bytes
from . tokens import generate_token




# Create your views here.
def home(request):
    
    return render(request, "registration/loginpage.html")

def signup(request):

    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        #Tests if email is @emory.edu
        mail = email.lower()
        at_index = mail.find('@')+1
        domain = mail[at_index:]
        if domain != 'emory.edu':
            messages.error(request, "Please enter @emory.edu email")
            return redirect('signup')

        #checks for email duplicates in system
        if User.objects.filter(email=email):
            messages.error(request, "Email already exists! Please try some other email")
            return redirect('signup')
        
        #makes sure password and confirmation password match
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
            return redirect('signup')
        
        
        myuser = User.objects.create_user(email, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.is_active = False

        myuser.save()

        messages.success(request,"Your Account has been successfully created. We have sent you a confirmation email, please confirm your email in order to activate your account")

        # Welcome Email
        subject = "Welcome to Research Match Login!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Research Match! \n Thank you for visiting our website. \n We have also sent you a confirmation email, please confirm your email address in order to activate your account. \n\n Thank you, \n Deadline Tech"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email

        current_site = get_current_site(request)
        email_subject = "Confirm your email @ Research Match Login!"
        message2 = render_to_string('email_confirmation.html',{
            
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })

        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('studentlogin')



    return render(request, "registration/loginpage.html")

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    
    else: 
        return render(request, 'activation_failed.html')
    

def studentlogin(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                firstname = user.first_name
                return render(request, reverse('profilepage'), {'firstname': firstname})
            
            else:
                messages.error(request, "User account is not confirmed. Please check your email for confirmation link.")
                return redirect('home')

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')


    return render(request, "registration/loginpage.html")

def lablogin(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                firstname = user.first_name
                return render(request, "profile.html", {'firstname': firstname})
            
            else:
                messages.error(request, "User account is not confirmed. Please check your email for confirmation link.")
                return redirect('home')

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')


    return render(request, "registration/loginpage.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('home')
