from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from profilepage.models import StudentProfile

def search(request):
    return render(request, 'search.html')

def search_profiles(request):
    if request.htmx:  # Check for the HTMX request header
        query = request.GET.get('q', '') 

        if len(query) > 0:
            # Search profiles by matching the query with first name, last name, or background fields
            profiles = StudentProfile.objects.filter(
                Q(firstname__icontains=query) | 
                Q(lastname__icontains=query) | 
                Q(background__icontains=query) |
                Q(labname__icontains=query)
            )
            # Render only the search results to a specific template for HTMX to swap in
            return render(request, 'search/list_profiles.html', {'profiles': profiles})
        else:
            # If query is empty, return an empty response to clear the results
            return HttpResponse('')

    else:
        # If it's not an HTMX request, raise a 404
        raise Http404('')

#Function to display the details of the profile
def profile_detail(request, id):
    StudentProfile = get_object_or_404(StudentProfile, id=id)

    #Check the type of profile and redirect it accordingly
    if StudentProfile.StudentProfile_BACKGROUND == "Student":
        return render(request, 'profilepage/StudentMain.html', {'StudentProfile': StudentProfile})
    elif StudentProfile.StudentProfile_BACKGROUND == "Mentor":
        return render(request, 'profilepage/LabMain.html', {'StudentProfile': StudentProfile})
    else: 
        raise Http404()
