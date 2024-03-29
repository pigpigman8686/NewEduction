"""NewEducation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from IndexPage import views as IndexPageViews
from LearningCondition import views as LearningConditionViews
from TeachingData import views as TeachingDataViews
from TeachingResult import views as TeachingResultViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_zzh/', IndexPageViews.index_zzh),
    path('index_lsj/', IndexPageViews.index_lsj),
    path('learning_condition/', LearningConditionViews.portrait),
    path('Student_course/', LearningConditionViews.course),
    path('Student_portrait/', LearningConditionViews.Student_protrait),
    path('course_resource/', LearningConditionViews.course_resource),
    path('path_plan/', LearningConditionViews.path_plan),
    path('teaching_data/', TeachingDataViews.catalog),
    path('teaching_result/', TeachingResultViews.analyse),
    path('jsontest/', LearningConditionViews.jsontest),
    path('Teacher_courses/', TeachingDataViews.Course),
    path('Teacher_protrait/', TeachingDataViews.Teacher_portrait),


]
