from django.shortcuts import render
from profilepage.models import StudentProfile
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def all_students(request):
    users_list = StudentProfile.objects.filter(background='S')  # Retrieve all users
    paginator = Paginator(users_list, 5)  # Paginator, 5 users per page

    page_number = request.GET.get('page')  # Get the page number from the request
    page_obj = paginator.get_page(page_number)  # Get the page

    return render(request, 'students.html', {'page_obj': page_obj})

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
            template_name='list_students.html',
            context={'page': page}
        )

    return render(request, 'list_students.html')

@login_required
def available_labs(request):
    current_user = request.user
    student_profile = StudentProfile.objects.get(user=current_user)
    student_skills = set(student_profile.skill_list())
    
    all_labs = StudentProfile.objects.filter(background='M')
    matching_labs = [lab for lab in all_labs if student_skills & set(lab.skills_list())]

    paginator = Paginator(matching_labs, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'available_labs.html', {'page_obj': page_obj})


