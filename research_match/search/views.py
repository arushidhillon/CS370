from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from profilepage.models import User
from django.core.paginator import Paginator

def search_students(request):
    if request.htmx:
      search = request.GET.get('q')
      page_num = request.GET.get('page', 1)

      if search:
          students = User.studentprofile.objects.filter(first_name__icontains=search)
      else:
          students = User.studentprofile.objects.none()
      page = Paginator(object_list=students, per_page=5).get_page(page_num)

      return render(
          request=request,
          template_name='partial_results.html',
          context={
              'page': page
          }
      )
    return render(request, 'partial_search.html')

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
