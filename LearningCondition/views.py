import copy
import json
from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.db.models import Count
from IndexPage.models import *
from django.db.models import Avg
from django.db.models.functions import *


# Create your views here.



def course(request):
    dict = {"name": "1zh"}
    return render(request, 'Student/Courses.html', dict)


def course_resource(request):
    return render(request, 'Student/CourseResources.html')


def path_plan(request):
    return render(request, 'Student/PathPlan.html')


def portrait(request):
    return render(request, 'component/Portrait.html')
