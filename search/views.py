from django.http import HttpResponse, Http404
from django.shortcuts import render
from profilepage.models import User
from profilepage.decorators import allowed_users

# Decorator to restrict access to the 'students' view to users with the 'lab' role only.
@allowed_users(allowed_roles=['lab'])
def students(request):
    return render(request, 'students.html')

# Decorator to restrict access to the 'students' view to users with the 'lab' role only.
@allowed_users(allowed_roles=['lab'])
def search_students(request):
    all = User.objects.all() # Retrieves all user objects from the database.

    if request.htmx:
        letters = request.GET.get('search_students') # Retrieves the user's search input
        if len(letters) > 0 :
            allprofiles = all.filter(first_name__icontains=letters) # Filters the User objects whose first name contains the search input.
            profiles = [ x for x in allprofiles if (x.studentprofile.is_student)] # Further filters to get profiles where the related student profile indicates they are a student.
            return render(request, 'list_students.html', {'students' : profiles})
        else:
            return HttpResponse('') # If the search input is empty, returns an empty HttpResponse.
    else:
        raise Http404()
