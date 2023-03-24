from django.shortcuts import render, redirect
from IndexPage import models

from django.shortcuts import render, redirect
from IndexPage import models
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.db.models import DateTimeField
from django.db.models import Count, Sum, Avg, F
from .models import *
from django.db.models import FloatField, Avg, Q
from django.db.models.functions import *
from django.db.models import IntegerField, Value
from django.db.models.functions import Cast
import pandas as pd
from django.db.models import Q
import json

def index(request):
    use_courseid = 224841013
    learn_answer = {

    }
    bbs_count_day = TStatBbsLog.objects.filter(courseid=use_courseid) \
        .filter(topic_id=0) \
        .annotate(date=TruncDate('last_modify_time')) \
        .values('date') \
        .annotate(count=Count('reply_id')) \
        .order_by('date')
    print(bbs_count_day)
    for item in bbs_count_day:
        huitie_work = item['count']
        ddaa = str(item['date'])
        learn_answer[ddaa] = huitie_work
    # 发帖
    bbs_count_days = TStatBbsLog.objects.filter(courseid=use_courseid) \
        .exclude(topic_id=0) \
        .annotate(date=TruncDate('last_modify_time')) \
        .values('date') \
        .annotate(count=Count('parent_id')).distinct() \
        .order_by('date')
    learn_topic = {

    }

    for item in bbs_count_days:
        fatie_works = item['count']
        ddaa = str(item['date'])
        learn_topic[ddaa] = fatie_works

    lesson_all = {

        "learn_answer": learn_answer,
        "learn_topic": learn_topic,

    }

    with open("data.json", "w") as f:
     json.dump(lesson_all, f)

    return render(request, "TeachingResult.html", lesson_all)


def get_data(request):
    obj = models.TStatWorkRelation.objects.filter(id=1).first()
    print(obj.id)
    return render(request, 'index.html', {'row': obj})
