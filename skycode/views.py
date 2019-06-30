from django.shortcuts import render
from skycode.models import *

# Create your views here.


def index(request):
    context = {'teachers': Teacher.objects.all(),
               'partners': Partner.objects.all(),
               'courses': Course.objects.all(),
               }
    return render(request, 'main.html', context)


def get_courses(request):
    context = {'courses': Course.objects.all()}
    return render(request, 'course.html', context)
