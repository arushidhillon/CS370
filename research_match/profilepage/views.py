
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Skills
from .forms import SkillForm

from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie

def hi(request):
    template = loader.get_template('StudentMain.html')
    return HttpResponse(template.render())

from .forms import SkillForm


def get_skill(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SkillForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        skill_input = form.cleaned_data['skill']
        p = Skills(skill_input)
        p.save()

            # return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SkillForm()

    return render(request, "StudentMain.html", {"form": form})


def get_skills(request):

    all_Skills = Skills.objects.all() #for all the records 
    # one_data = userdetails.objects.get(pk=1) # 1 will return the first item change it depending on the data you want 
    allskills={
       
      'skills':all_Skills,
    #   'one_data':one_data,
    
    } 

    return render(request, 'StudentMain.html', allskills)
