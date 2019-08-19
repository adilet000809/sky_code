from rest_framework import serializers
from .models import Teacher, Course


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('firstName', 'lastName', 'position', 'description', 'email', 'experience', 'image')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'teacher', 'start', 'duration', 'time', 'price')
