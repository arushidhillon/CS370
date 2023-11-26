from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from profilepage.models import User

def search_students(request):
    if request.htmx:
        letters = request.GET.get('search_students')
        if len(letters) > 0:
            students = User.StudentProfile.objects.filter(first_name__contains=letters, is_student=True).exclude(username=request.user)
            return render(request, 'list_searchuser.html', { 'students' : students })
        else:
            return HttpResponse('')
    else:
        raise Http404()

def search_labs(request):
    if request.htmx:
        letters = request.GET.get('search_labs')
        if len(letters) > 0:
            labs = User.StudentProfile.objects.filter(labname__contains=letters).exclude(username=request.user)
            return render(request, 'list_searchuser.html', { 'labs' : labs })
        else:
            return HttpResponse('')
    else:
        raise Http404()

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
