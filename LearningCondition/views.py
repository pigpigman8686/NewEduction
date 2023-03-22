from django.shortcuts import render, redirect
from IndexPage import models

from django.db.models import Count, F
# from .models import *
from django.db.models import FloatField

from django.db.models import IntegerField, Value
from django.db.models.functions import Cast

# Create your views here.


def course(request):

    return render(request, 'Student/Courses.html')


def course_resource(request):

    return render(request, 'Student/CourseResources.html')


def path_plan(request):

    return render(request, 'Student/PathPlan.html')


def portrait(request):
    return render(request, 'component/Portrait.html')
