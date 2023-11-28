from django.shortcuts import render
from profilepage.models import StudentProfile
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

@login_required
def all_students(request):
    users_list = StudentProfile.objects.filter(background='S')  # Retrieve all users
    paginator = Paginator(users_list, 5)  # Paginator, 10 users per page

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
            template_name='form_searchstudents.html',
            context={'page': page}
        )

    return render(request, 'form_searchstudents.html')


