from django.shortcuts import render
from django.http import HttpResponse, Http404
from profilepage.models import User
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def all_students(request):
    if request.htmx:
        all = User.objects.all()
        all_students = all.filter(groups__name ='student')  # Retrieve all users

        return render(request, 'students.html', {'students': all_students})

@login_required
def search_students(request):
    if request.htmx:
        letters = request.GET.get('search_students')
        if len(letters) > 0:
            students = User.objects.filter(first_name__contains=letters, groups__name = 'student').exclude(username=request.user)
            return render(request, 'list_students.html', {'users' : students})
        else:
            return HttpResponse('')
    else:
        raise Http404()


