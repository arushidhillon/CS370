from django.http import HttpResponse, Http404
from django.shortcuts import render
from profilepage.models import User
from profilepage.decorators import allowed_users

@allowed_users(allowed_roles=['lab'])
def students(request):
    return render(request, 'students.html')


@allowed_users(allowed_roles=['lab'])
def search_students(request):
    all = User.objects.all()
    all_students = all.filter(groups__name ='student')

    if request.htmx:
        letters = request.GET.get('search_students')
        if len(letters) > 0 :
            profiles = all_students.filter(first_name__icontains=letters)
            return render(request, 'list_students.html', {'students' : profiles})
        else:
            return HttpResponse('')
    else:
        raise Http404()
