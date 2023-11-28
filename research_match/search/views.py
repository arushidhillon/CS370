from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from profilepage.models import StudentProfile
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def search_students(request):
    if request.htmx:
        search = request.GET.get('q')
        page_num = request.GET.get('page', 1)

        if search:
            # Filter student profiles based on search query and is_student property
            students = StudentProfile.objects.filter(
                Q(first_name__icontains=search) | 
                Q(last_name__icontains=search),
                is_student=True
            )
        else:
            students = StudentProfile.objects.filter(is_student=True)

        page = Paginator(object_list=students, per_page=5).get_page(page_num)

        return render(
            request=request,
            template_name='form_searchstudents.html',
            context={'page': page}
        )

    return render(request, 'form_searchstudents.html')

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
