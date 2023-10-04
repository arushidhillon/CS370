from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

from django.http import HttpResponse
from django.template import loader

def hi(request):
    template = loader.get_template('StudentMain.html')
    return HttpResponse(template.render())