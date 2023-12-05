from django.shortcuts import render
from django.http import HttpResponse, Http404
from profilepage.models import User
from profilepage.decorators import allowed_users

# This decorator restricts access to the 'students' view to users with the 'lab' role.
@allowed_users(allowed_roles=['lab'])
def students(request):
    return render(request, 'students.html')


# This function handles the searching of students.
def search_students(request):
    all = User.objects.all() # Retrieves all User objects from the database.
    all_students = all.filter(groups__name ='student') # Filters the User objects to include only those in the 'student' group.

    if request.htmx:
        letters = request.GET.get('search_students')
        if len(letters) > 0 : # Checks if the search input is not empty.
            profiles = all_students.objects.filter(first_name__icontains=letters).exclude(username=request.user) # Filters the student profiles based on the search input in the first name field and excludes the current user from the results.
            return render(request, 'list_students.html', {'students' : profiles})
        else:
            return HttpResponse('') # Returns an empty HttpResponse if there is no search input.
    else:
        raise Http404()


