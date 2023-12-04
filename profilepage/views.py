from datetime import timezone
from itertools import chain
from django.forms import ValidationError
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader
from django.views import View

from inbox.forms import InboxNewMessageForm
from inbox.models import Conversation
from .models import StudentProfile
from django.views.generic.list import ListView

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
from .tokens import generate_token
from django.contrib.auth.password_validation import validate_password
from .forms import UserUpdateForm, ProfileUpdateForm
from .decorators import allowed_users, unauthenticated_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import UserUpdateForm, ProfileUpdateForm, LabUpdateForm, Picform, Skillform, Courseform, Docform, BioForm, GpaForm
from django.views.generic import ListView
import random

from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.validators import URLValidator


@ensure_csrf_cookie
# This function leads the user to the homepage of Research Match.
def home(request):
    return render(request, "home.html")


# This function registers the user and stores their information. The user can choose to either sign up as a student or a lab.
def signup(request):
    if request.method == "POST":
        # Requests information inputted
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Tests if email is @emory.edu
        mail = email.lower()
        at_index = mail.find('@') + 1
        domain = mail[at_index:]
        if domain != 'emory.edu':
            messages.error(request, "Please enter @emory.edu email")
            return redirect('signup')

        # checks for email duplicates in system
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists! Please try some other email")
            return redirect('signup')

        # checks to make sure password is 8 characters long, not entirely numerical/alphabetical, or too common
        if pass1 is not None:
            try:
                validate_password(pass1)
            except ValidationError as e:

                # If the password is not strong, the errors will display why.
                for error in e.error_list:
                    messages.error(request, error)
                if e.error_list is not None:
                    return redirect('signup')

        # makes sure password and confirmation password match
        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!")
            return redirect('signup')

        # stores information in database using create_user function
        myuser = User.objects.create_user(email, email, pass1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.is_active = False

        myuser.save()
        # Add group to user
        signup_type = request.POST.get('signup_type')
        if signup_type == 'student':
            group_name = 'student'
            group, created = Group.objects.get_or_create(name=group_name)
            myuser.groups.add(group)

        elif signup_type == 'lab':
            group_name = 'lab'
            group, created = Group.objects.get_or_create(name=group_name)
            myuser.groups.add(group)
        myuser.save()
        messages.success(request,
                         "Your Account has been successfully created. We have sent you a confirmation email, please confirm your email in order to activate your account. You may need to look in the spam folder.")

        # Welcome Email
        # subject = "Welcome to Research Match Login!"
        # message = "Hello " + myuser.first_name + "! \n" + "Welcome to Research Match! \n Thank you for visiting our website. We hope you find the research opportunities you're looking for. \n We have also sent you a confirmation email, please confirm your email address in order to activate your account. This may be located in the spam folder. \n\n Thank you, \n Deadline Tech"
        # from_email = 'deadline.tech@research-match.com'
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation and Welcome Email

        current_site = get_current_site(request)
        email_subject = "Welcome to Research Match! Please Confirm your email to Login!"
        message2 = render_to_string('email_confirmation.html', {

            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })

        email = EmailMessage(
            email_subject,
            message2,
            "deadline.tech@research-match.com",
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('studentlogin')

    return render(request, "registration/loginpage.html")


# This function activates a user's registered account by using a customized token that verifies the user's email address.
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
        return redirect('studentlogin')

    else:
        return render(request, 'activation_failed.html')


# This function logs the student user in after they activate their account.
@allowed_users(allowed_roles=['student'])
def studentlogin(request):
    if 'studentlog' in request.POST:
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # This redirects the user to the login page if they aren't loggged in and are in a different page.
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    myuser = user.studentprofile.get_user_name()
                    return redirect('/profile/' + myuser)

            else:
                messages.error(request, "User account is not confirmed. Please check your email for confirmation link.")
                return redirect('studentlogin')

        else:
            if User.objects.filter(username=email).exists():
                messages.error(request, "The Password you entered is incorrect. Please try again or reset password.")
                return redirect('studentlogin')
            else:
                messages.error(request,
                               "The email you entered does not match our records. Please double-check and try again.")
                return redirect('studentlogin')

    return render(request, "registration/loginpage.html")


# same code as student login, doesn't lead to lab profile page or stores in different table for now
@allowed_users(allowed_roles=['lab'])
def lablogin(request):
    if 'lablog' in request.POST:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                # This redirects the user to the login page if they aren't loggged in and are in a different page.
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    myuser = user.studentprofile.get_user_name()
                    return redirect('/profile/' + myuser)

            else:
                messages.error(request, "User account is not confirmed. Please check your email for confirmation link.")
                return redirect('lablogin')

        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, "The Password you entered is incorrect. Please try again or reset password.")
                return redirect('lablogin')
            else:
                messages.error(request,
                               "The email you entered does not match our records. Please double-check and try again.")
                return redirect('lablogin')

    return render(request, "registration/loginpage.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!")
    return redirect('signup')


@allowed_users(allowed_roles=['student'])
def studenthomepage(request):
    return render(request, "StudentMain.html")


def settings(request):
    return render(request, "Settings.html")


@allowed_users(allowed_roles=['student'])
def matches(request, pk):
    pk += '@emory.edu'

    user_object = User.objects.get(username=pk)
    user_profile = StudentProfile.objects.get(user=user_object)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
    }
    return render(request, 'matches.html', context)

@allowed_users(allowed_roles=['lab'])
def labpicedit(request):
    return render(request, "editprofilepic.html")


@allowed_users(allowed_roles=['lab'])
def labhomepage(request):
    return render(request, "LabMain.html")


@allowed_users(allowed_roles=['lab'])
def students(request):
    return render(request, 'students.html')


@allowed_users(allowed_roles=['lab'])
def matchedstudents(request, pk):
    pk += '@emory.edu'
    user_object = User.objects.get(username=pk)
    user_profile = StudentProfile.objects.get(user=user_object)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
    }
    return render(request, "matchedstudents.html", context)


# from .forms import SkillForm

from .models import StudentProfile


@allowed_users(allowed_roles=['student'])
def studentprofile(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.studentprofile)

        if u_form.is_valid() and p_form.is_valid():
            # if p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile/' + myuser)


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.studentprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'skill.html', context)


@allowed_users(allowed_roles=['lab'])
def labprofile(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = LabUpdateForm(request.POST,
                               request.FILES,
                               instance=request.user.studentprofile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile/' + myuser)

        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = LabUpdateForm(instance=request.user.studentprofile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }
        return render(request, 'mentoredit.html', context)


@allowed_users(allowed_roles=['lab'])
def labpictureupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = Picform(request.POST,
                         request.FILES,
                         instance=request.user.studentprofile)
        # if request.FILES.get('profile_pic') is None:
        #     if pic_form.is_valid():
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            messages.success(request, f'Your account has been updated!')
            image_url = request.POST.get('profile_pic', None)
            if image_url is not None :
                instance.image_url = image_url
            else:
                instance.image_url = 'https://static.thenounproject.com/png/5034901-200.png'
            instance.save()
            return redirect('profile/' + myuser)




        else:
            p_form = Picform(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'picture.html', context)

@allowed_users(allowed_roles=['student'])
def studentpictureupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = Picform(request.POST,
                         request.FILES,
                         instance=request.user.studentprofile)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            messages.success(request, f'Your account has been updated!')
            image_url = request.POST.get('profile_pic', None)
            if image_url is not None :
                instance.image_url = image_url
            else:
                instance.image_url = 'https://static.thenounproject.com/png/5034901-200.png'
            instance.save()
            return redirect('profile/' + myuser)

        else:
            p_form = Picform(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'picture.html', context)

@allowed_users(allowed_roles=['lab'])
def labskillsupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = Skillform(request.POST,
                           instance=request.user.studentprofile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile/'+myuser)  # Send back to profile 
        
        else:
            p_form = Skillform(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'editprofilepic.html', context)

@allowed_users(allowed_roles=['student'])
def studentskillsupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = Skillform(request.POST, instance=request.user.studentprofile)
        # if request.FILES.get('profile_pic') is None:
        #     if pic_form.is_valid():
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile/' + myuser)

        else:
            p_form = Skillform(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'editprofilepic.html', context)

@allowed_users(allowed_roles=['lab'])
def labcourseupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = Courseform(request.POST,
                            instance=request.user.studentprofile)
        # if request.FILES.get('profile_pic') is None:
        #     if pic_form.is_valid():
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile/'+myuser)  # Send back to profile
        
        else:
            p_form = Courseform(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'editprofilepic.html', context)

@allowed_users(allowed_roles=['student'])
def studentcourseupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = Courseform(request.POST,
                            instance=request.user.studentprofile)
        # if request.FILES.get('profile_pic') is None:
        #     if pic_form.is_valid():
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile/' + myuser)

        else:
            p_form = Courseform(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'editprofilepic.html', context)

@allowed_users(allowed_roles=['lab'])
def labbioupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = BioForm(request.POST,
                         instance=request.user.studentprofile)
        # if request.FILES.get('profile_pic') is None:
        #     if pic_form.is_valid():
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile/'+myuser)  # Send back to profile
        
        else:
            p_form = BioForm(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'editprofilepic.html', context)

@allowed_users(allowed_roles=['student'])
def studentbioupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = BioForm(request.POST,
                         instance=request.user.studentprofile)
        # if request.FILES.get('profile_pic') is None:
        #     if pic_form.is_valid():
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile/'+myuser)  # Send back to profile  
        
        else:
            p_form = BioForm(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'editprofilepic.html', context)

@allowed_users(allowed_roles=['lab'])
def labdocupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = Docform(request.POST,
                         request.FILES,
                         instance=request.user.studentprofile)
        # if request.FILES.get('profile_pic') is None:
        #     if pic_form.is_valid():
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            doc_url = request.POST.get('document_url', None)
            if doc_url is not None :
                instance.doc_url = doc_url
            instance.save()
            return redirect(f'profile/'+myuser)  # Send back to profile  
        
        else:
            p_form = Docform(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'document.html', context)

@allowed_users(allowed_roles=['student'])
def studentdocupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = Docform(request.POST,
                         request.FILES,
                         instance=request.user.studentprofile)
        # if request.FILES.get('profile_pic') is None:
        #     if pic_form.is_valid():
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            doc_url = request.POST.get('document_url', None)
            if doc_url is not None :
                instance.doc_url = doc_url
            instance.save()
            return redirect('profile/'+myuser)  # Send back to profile  
        
        else:
            p_form = Docform(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'document.html', context)


def profile(request, pk):
    pk += '@emory.edu'
    user_object = User.objects.get(username=pk)
    user_profile = StudentProfile.objects.get(user=user_object)

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
    }

    if user_profile.is_student:
        return render(request, 'StudentMain.html', context)
    elif user_profile.is_lab:
        return render(request, 'LabMain.html', context)
    else:
        return render(request, 'home.html', context)

# Creates match between a student and a lab and vice versa.
def match(request, pk):
    pk += '@emory.edu'
    user_object = User.objects.get(username=pk)
    user_profile = StudentProfile.objects.get(user=user_object)

    if (user_profile.is_lab and request.user.studentprofile.is_student) or (user_profile.is_student and request.user.studentprofile.is_lab):
        request.user.studentprofile.matches.add(user_profile)
        request.user.studentprofile.save()

    if user_profile.is_lab:
        messages.success(request, (f"You Have Successfully Matched With a Lab!"))
    else:
        messages.success(request, (f"You Have Successfully Matched With a Student"))

    return redirect(request.META.get("HTTP_REFERER"))

# Allows labs and students to unmatch each other.
def unmatch(request, pk):
    pk += '@emory.edu'
    user_object = User.objects.get(username=pk)
    user_profile = StudentProfile.objects.get(user=user_object)

    if (user_profile.is_lab and request.user.studentprofile.is_student) or (user_profile.is_student and request.user.studentprofile.is_lab):
        request.user.studentprofile.matches.remove(user_profile)
        request.user.studentprofile.save()

    if user_profile.is_lab:
        messages.success(request, (f"You Have Successfully Unmatched With a Lab!"))
    else:
        messages.success(request, (f"You Have Successfully Unmatched With a Student"))

    return redirect(request.META.get("HTTP_REFERER"))

        

# This function will serve as the matching algorithm for both lab and students.
# It will match them through their registered skill, course, and gpa.
def MatchAlgorithm(request):
    user_profile = request.user.studentprofile
    user_matching_list = user_profile.matches.all()

    matching_by_skill = user_profile.skill
    matching_by_course = user_profile.course
    matching_by_gpa = user_profile.gpa

    all_users = StudentProfile.objects.all()

    if user_profile.is_student:
        lab_req_c = all_users.filter(course__in=matching_by_course)
        lab_req_s = all_users.filter(skill__in=matching_by_skill)
        lab_req_g = all_users.filter(gpa__lte=matching_by_gpa)

        all_labs = [ x for x in all_users if (x.is_lab)]
        new_suggestions_list = [ x for x in all_labs if (x not in user_matching_list)]
        final_suggestions_list = [x for x in new_suggestions_list if (x in lab_req_c or x in lab_req_s or x in lab_req_g)]

        context = {
        'user_profile': user_profile,
        'final_suggestions_list': final_suggestions_list,
        }
        return render(request, 'opportunities.html', context)
    else:
        lab_req_c = all_users.filter(course__in=matching_by_course)
        lab_req_s = all_users.filter(skill__in=matching_by_skill)
        lab_req_g = all_users.filter(gpa__gte=matching_by_gpa)

        all_students = [ x for x in all_users if (x.is_student)]
        new_suggestions_list = [ x for x in all_students if (x not in user_matching_list)]
        final_suggestions_list = [x for x in new_suggestions_list if (x in lab_req_c or x in lab_req_s or x in lab_req_g)]
        context = {
        'user_profile': user_profile,
        'final_suggestions_list': final_suggestions_list,
        }

        return render(request, 'students.html', context)
    
# This function allows a lab to delete all it's matches in order to start over as a new lab.
@allowed_users(allowed_roles=['lab'])
def remove(request):
    all_matches = StudentProfile.matches.all()
    all_matched = StudentProfile.matched_by.all()

    for x in all_matches:
        request.user.studentprofile.remove(x)
        request.user.studentprofile.save()
    
    for y in all_matched:
        request.user.studentprofile.remove(all_matched)
        request.user.studentprofile.save()

    messages.success(request, (f"You Have Successfully UnMatched All Students"))
    return redirect(request.META.get("HTTP_REFERER"))

def labgpaupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = GpaForm(request.POST,
                         instance=request.user.studentprofile)
        # if request.FILES.get('profile_pic') is None:
        #     if pic_form.is_valid():
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect(f'profile'+myuser)  # Send back to profile

        else:
            p_form = GpaForm(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'editprofilepic.html', context)


def studentgpaupdate(request):
    myuser = request.user.studentprofile.get_user_name()
    if request.method == 'POST':
        p_form = GpaForm(request.POST, instance=request.user.studentprofile)
        # if request.FILES.get('profile_pic') is None:
        #     if pic_form.is_valid():
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            # TODO: apply to other forms
            return redirect(f'profile'+myuser)  # Send back to profile

        else:
            p_form = GpaForm(instance=request.user.studentprofile)

        context = {
            'p_form': p_form
        }
        return render(request, 'editprofilepic.html', context)

# View to handle creation of new messages
@login_required     
def new_message_match(request, recipient_id):
    recipient = get_object_or_404( User, id=recipient_id) # Get the recipient user object
    new_message_form = InboxNewMessageForm() # Instantiate a new message form
    
    if request.method == 'POST':
        form = InboxNewMessageForm(request.POST)
        if form.is_valid(): # Validate the form
            message = form.save(commit=False)

            # encrypt message
            message_original = form.cleaned_data['body']
            message_bytes = message_original.encode('utf-8')
            message_encrypted = f.encrypt(message_bytes)
            message_decoded = message_encrypted.decode('utf-8')
            message.body = message_decoded
            
            message.sender = request.user # Set the sender of the message
            my_conversations = request.user.conversations.all()
            try:
                # Check if a conversation already exists with the recipient
                for c in my_conversations:
                    if recipient in c.participants.all():
                        message.conversation = c
                        message.save()
                        c.lastmessage_created = timezone.now()
                        c.is_seen = False
                        c.save()
                        return redirect('inbox', c.id) # Redirect to the conversation
            except:
                print("oops")
            # Create a new conversation if none exists
            new_conversation = Conversation.objects.create()
            new_conversation.participants.add(request.user, recipient)
            new_conversation.save()
            message.conversation = new_conversation
            message.save() 
            return redirect('inbox', new_conversation.id)
    
    context = {
        'recipient': recipient,
        'new_message_form': new_message_form
    }
    return render(request, 'form_newmessage_match.html', context)  # Render the new message form
