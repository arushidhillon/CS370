from django.shortcuts import render
from django.http import HttpResponse, Http404
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


@allowed_users(allowed_roles=['student'])
def opportunities(request):
    return render(request, "opportunities.html")


@allowed_users(allowed_roles=['student'])
def search_opportunities(request): 
    all = User.objects.all()
    all_opportunities = all.filter(groups__name='lab')

    if request.htmx:
        letters = request.GET.get('search_labs')
        if len(letters) > 0:
            labs = all_opportunities.filter(background__icontains=letters | all_opportunities.filter(labname__icontains=letters) | all_opportunities.filter(skills__icontains=letters))
            return render(request, 'list_opportunities.html', {'labs' : labs})
        else:
            return HttpResponse('')
    else:
        raise Http404()