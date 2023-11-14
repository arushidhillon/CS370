from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from profilepage.models import StudentProfile

def search_profiles(request):
    if request.headers.get('HX-Request'):  # Check for the HTMX request header
        query = request.GET.get('q', '') 

        if query:
            # Search profiles by matching the query with first name, last name, or background fields
            profiles = StudentProfile.objects.filter(
                Q(firstname__icontains=query) | 
                Q(lastname__icontains=query) | 
                Q(background__icontains=query) |
                Q(labname_icontains=query)
            )
            # Render only the search results to a specific template for HTMX to swap in
            return render(request, 'profiles/search.html', {'profiles': profiles})
        else:
            # If query is empty, return an empty response to clear the results
            return HttpResponse('')

    else:
        # If it's not an HTMX request, raise a 404
        raise Http404('')

#Function to list all profiles 
def list_profiles(request):
    StudentProfile = StudentProfile.objects.all()
    return render(request, 'list_profiles.html', {'StudentProfile': StudentProfile})

#Function to display the details of the profile
def profile_detail(request):
    StudentProfile = get_object_or_404(StudentProfile, id=id)
    return render(request, 'StudentMain.html', {'StudentProfile': StudentProfile})