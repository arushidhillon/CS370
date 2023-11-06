from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.db.models import Q
from profile.models import User
from .models import *

def search_labs(request):
    if request.htmx:
        result = request.GET.get('search_labs')
        if len(result) > 0:
            # Search by background, first name, or last name
            users = User.objects.filter(
                Q(background__icontains=result) |
                Q(firstname__icontains=result) |
                Q(lastname__icontains=result)
            ).exclude(username=request.user.username)
            return render(request, 'search/list_searchlabs.html', {'users': users})
        else:
            return HttpResponse('Please enter a valid search.')
    else:
        raise Http404()