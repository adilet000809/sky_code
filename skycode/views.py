from django.http import JsonResponse
from django.shortcuts import render
from skycode.models import *
from rest_framework import viewsets

from skycode.serializers import TeacherSerializer, CourseSerializer


class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


def index(request):
    context = {'teachers': Teacher.objects.all(),
               'partners': Partner.objects.all(),
               'courses': Course.objects.all(),
               'news': News.objects.all(),
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
        return JsonResponse({'message': 'successful'}, safe=False)


def enroll_course(request):
    if request.is_ajax():
        name = request.GET['name']
        telephone = request.GET['telephone']
        email = request.GET['email']
        comment = request.GET['comment']
        Request.objects.create(name=name, phone=telephone, email=email, comments=comment).save()
        return JsonResponse({'message': 'successful'}, safe=False)

