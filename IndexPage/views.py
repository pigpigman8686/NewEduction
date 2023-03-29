from django.shortcuts import render, redirect
from IndexPage import models
from django.http import JsonResponse

from django.db.models import Count, F
from .models import *
from datetime import datetime, timedelta

from django.db.models import FloatField, Avg, Q
from django.db.models.functions import *
from django.db.models import IntegerField, Value
from django.db.models import *
from django.db.models.functions import Cast
import pandas as pd
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


import json
def index_zzh(request):


    learn_curve = {

    }

    word_cloud = []

    like_job = []

    hot_act_count = {

    }

    lesson_act_type = {

    }

    lesson_act_time = {

    }


    # lesson_act_type
    use_courseid = 224841013
    count_by_type = TStatActivityLog.objects.filter(courseid=use_courseid).values('dtype').annotate(
        count=Count('dtype'))
    for item in count_by_type:
        lesson_act_type[item['dtype']] = item['count']

    # lesson_act_time
    use_courseid = 224841013
    activity_count_by_month = TStatActivityLog.objects.filter(courseid=use_courseid) \
        .annotate(month=ExtractMonth('attend_time')) \
        .values('month') \
        .annotate(count=Count('id')) \
        .order_by('month')

    for item in activity_count_by_month:
        lesson_act_time[item['month']] = item['count']

    # act_count
    use_courseid = 222602451
    counts_by_month = (
        TStatJobFinish.objects
        .filter(courseid=use_courseid)
        .annotate(month=ExtractMonth('insert_time'), hour=ExtractHour('insert_time'))
        .annotate(
            hour_group=Case(
                When(hour__lt=4, then=1),
                When(hour__lt=8, then=2),
                When(hour__lt=12, then=3),
                When(hour__lt=16, then=4),
                When(hour__lt=20, then=5),
                default=6,
                output_field=models.IntegerField(),
            )
        )
        .values('month', 'hour_group')
        .annotate(count=Count('id'))
        .order_by('month', 'hour_group')
    )

    for one in counts_by_month:
        month = one['month']
        hour = one['hour_group']
        count = one['count']
        if month not in hot_act_count:
            index = 1
            hot_act_count[month] = []
        for i in range(index, hour + 1):
            if i < hour:
                hot_act_count[month].append(0)
            else:
                index = hour + 1
                hot_act_count[month].append(count)

    # like_job
    use_courseid = 222602451
    order = 1
    job_like_id = TStatJobFinish.objects.filter(courseid=use_courseid, insert_time__month=3).values('job_id').annotate(
        count=Count('job_id')).distinct().order_by('-count').all()[:5]
    for item in job_like_id:
        job_id = item['job_id']
        count = item['count']
        like_job.append({"name": TStatCourseJob.objects.filter(job_id=job_id).values_list('name', flat=True).first(),
                         "count": count})
        order += 1

    # word_cloud
    use_courseid = 222602451
    use_course_all = list(
        TStatJobFinish.objects.filter(courseid=use_courseid, insert_time__month=3).values_list('job_id', flat=True))
    job_all = TStatCourseJob.objects.filter(job_id__in=use_course_all).values('name').annotate(count=Count('job_id'))
    for item in job_all:
        word_cloud.append({"name": item['name'], "count": item['count']})

    # learn_curve
    use_courseid = 222602451
    activity_count_by_month = TStatCourseJob.objects.filter(courseid=use_courseid) \
        .annotate(month=ExtractMonth('insert_time')) \
        .values('month') \
        .annotate(count=Count('job_id')) \
        .order_by('month')

    for item in activity_count_by_month:
        learn_curve[item['month']] = item['count']

    course_all = {
        "use_courseid": 224841013,
        "lesson_act_time": lesson_act_time,
        "lesson_act_type": lesson_act_type,
        "hot_act_count": hot_act_count,
        "like_job": like_job,
        "word_cloud": word_cloud,
        "learn_curve": learn_curve
    }

    # with open("data.json", "w") as f:
    #     json.dump(course_all, f)

    return render(request, 'TeachingResult.html', course_all)


def index_qjh(request):
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
