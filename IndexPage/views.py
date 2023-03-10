from django.shortcuts import render, redirect
from IndexPage import models

from django.db.models import Count, F
from .models import *
from django.db.models import FloatField

from django.db.models import IntegerField, Value
from django.db.models.functions import Cast
def index(request):
    #找成绩前40%的peisonid
    students = TStatStudentScore.objects.filter(courseid='222675513').annotate(score_float=Cast('score', FloatField())).order_by('-score_float')
    top_students_count = int((students.count() / 10)*4)
    top_students=list(students[:top_students_count].values_list('personid', flat=True))

    #用personid找前50%的job_id
    jobs = TStatJobFinish.objects.filter(personid__in=top_students).values_list('job_id', flat=True)

    #用job_id找任务点名称
    name_ues=TStatCourseJob.objects.filter(job_id__in=jobs)

    name_count = name_ues.values('name').annotate(job_count=Count('job_id')).order_by('-job_count')
    top_names_count = int(name_count.count() * 0.3)


    top_names = name_count[:top_names_count].values_list('name', flat=True)
    # print("需要掌握的任务点名称&&成绩前40%的学生都在学习什么:")
    # print(top_names,"\n")


    #################
    # 找成绩前40~60%的peisonid
    students = TStatStudentScore.objects.filter(courseid='222675513').annotate(
        score_float=Cast('score', FloatField())).order_by('-score_float')
    top_students_count1 = int((students.count() / 10) * 4)
    top_students_count2 = int((students.count() / 10) * 6)
    top_students = list(students[top_students_count1-1:top_students_count2 ].values_list('personid', flat=True))

    # 用personid找前50%的job_id
    jobs = TStatJobFinish.objects.filter(personid__in=top_students).values_list('job_id', flat=True)

    # 用job_id找任务点名称
    name_ues = TStatCourseJob.objects.filter(job_id__in=jobs)

    name_count = name_ues.values('name').annotate(job_count=Count('job_id')).order_by('-job_count')
    top_names_count = int(name_count.count() * 0.3)

    top_names = name_count[:top_names_count].values_list('name', flat=True)
    # print("需要熟悉的任务点名称:")
    # print(top_names,"\n")

    #################
    # 找成绩前40~60%的peisonid
    students = TStatStudentScore.objects.filter(courseid='222675513').annotate(
        score_float=Cast('score', FloatField())).order_by('-score_float')
    top_students_count2 = int((students.count() / 10) * 6)
    top_students = list(students[top_students_count2-1:].values_list('personid', flat=True))

    # 用personid找前50%的job_id
    jobs = TStatJobFinish.objects.filter(personid__in=top_students).values_list('job_id', flat=True)

    # 用job_id找任务点名称
    name_ues = TStatCourseJob.objects.filter(job_id__in=jobs)

    name_count = name_ues.values('name').annotate(job_count=Count('job_id')).order_by('-job_count')
    top_names_count = int(name_count.count() * 0.3)

    top_names = name_count[:top_names_count].values_list('name', flat=True)
    # print("需要了解的任务点名称:")
    # print(top_names, "\n")

    #####总讨论次数,发帖次数,回帖次数
    talk_person_use = TStatBbsLog.objects.filter(personid=111946336)
    fatie_count = talk_person_use.annotate(topic_id_int=Cast('topic_id', IntegerField())).filter(topic_id_int__gt=0)
    huitie_count = talk_person_use.annotate(reply_id_int=Cast('reply_id', IntegerField())).filter(reply_id_int__gt=0)
    print("学生总讨论次数", TStatBbsLog.objects.count())
    print("学生总发帖次数", TStatBbsLog.objects.annotate(topic_id_int=Cast('topic_id', IntegerField())).filter(topic_id_int__gt=0).count())
    print("学生总回帖次数", TStatBbsLog.objects.annotate(reply_id_int=Cast('reply_id', IntegerField())).filter(reply_id_int__gt=0).count())
    print("\n")

    print("id为111946336学生总讨论次数", talk_person_use.count())
    print("id为111946336学生总发帖次数", fatie_count.count())
    print("id为111946336学生总回帖次数", huitie_count.count())
    print("\n")


    #####总提交作业数
    work_person_use=TStatWorkAnswer.objects.filter(personid=111943630)
    work_person_id= list(work_person_use.values_list('courseid',flat=True))
    fabu_work_person=TStatWorkRelation.objects.filter(courseid__in=work_person_id).count()
    print("课程/设置作业数",TStatWorkLibrary.objects.count())
    print("课程/发布总作业数", TStatWorkRelation.objects.count())
    print("课程/总共提交作业数", TStatWorkAnswer.objects.count())
    print("发布给id为111943630学生的作业数为:",fabu_work_person)
    print("id为111943630学生提交作业数", work_person_use.count())
    ##求个体课程提交作业率,总提交率
    work_person_use2=TStatWorkAnswer.objects.filter(personid=111943630).filter(courseid=222602451).values('id').distinct().count()
    work_count=TStatWorkRelation.objects.filter(courseid=222602451).values('id').distinct().count()
    print("id为222808035的学生在id为222602451课程中提交作业率为:", work_person_use2/work_count)
    print("\n")





    #####总提交考试数
    exam_person_use = TStatExamAnswer.objects.filter(personid=111944552)
    exam_person_id = list(exam_person_use.values_list('courseid', flat=True))
    fabu_work_person = TStatWorkRelation.objects.filter(courseid__in=exam_person_id).count()
    print("课程/设置考试数", TStatExamLibrary.objects.count())
    print("课程/发布总考试数", TStatExamRelation.objects.count())
    print("课程/总共提交考试数", TStatExamAnswer.objects.count())
    print("发布给id为111943630学生的考试数为:",fabu_work_person)
    print("id为111944552学生提交考试数", exam_person_use.count())
    exam_person_use2=TStatExamAnswer.objects.filter(personid=111945146).filter(courseid=222820410).values('id').distinct().count()
    exam_count=TStatExamRelation.objects.filter(courseid=222820410).values('id').distinct().count()
    print("id为111945146的学生在id为222820410课程中提交考试率为:", exam_person_use2/exam_count*100, "%")
    print("\n")






    return render(request, 'index.html')
def get_data(request):
    obj = models.TStatWorkRelation.objects.filter(id=1).first()
    print(obj.id)
    return render(request, 'index.html', {'row': obj})
