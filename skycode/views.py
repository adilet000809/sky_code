from django.http import JsonResponse
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


def ask_question(request):
    if request.is_ajax():
        name = request.GET['name']
        email = request.GET['email']
        question = request.GET['question']
        Question.objects.create(name=name, email=email, question=question).save()
        return JsonResponse({'mesasge': 'successful'}, safe=False)

