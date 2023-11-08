from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from .models import SearchQuery
from profilepage.models import User

def search_labs(request):
    if request.htmx:
        result = request.GET.get('search_user', '').strip()
        if result:
            # Log the search query
            SearchQuery.objects.create(user=request.user, query=result)

            # Perform the search
            users = User.objects.filter(
                Q(background__icontains=result) |
                Q(firstname__icontains=result) |
                Q(lastname__icontains=result)
            ).exclude(username=request.user.username)
            return render(request, 'search/list_searchlabs.html', {'users': users})
        else:
            return HttpResponse('Please enter a valid search query.')
    else:
        return HttpResponse('This endpoint only responds to HTMX requests.')