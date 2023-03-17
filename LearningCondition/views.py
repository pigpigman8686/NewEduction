from django.shortcuts import render, redirect
from IndexPage import models

from django.db.models import Count, F
# from .models import *
from django.db.models import FloatField

from django.db.models import IntegerField, Value
from django.db.models.functions import Cast

# Create your views here.


def portrait(request):
    message = {}
    # 找成绩前40%的peisonid
    students = models.TStatStudentScore.objects.filter(courseid='222675513').annotate(
        score_float=Cast('score', FloatField())).order_by('-score_float')
    top_students_count = int((students.count() / 10) * 4)
    top_students = list(students[:top_students_count].values_list('personid', flat=True))


    # 用personid找前50%的job_id
    jobs = models.TStatJobFinish.objects.filter(personid__in=top_students).values_list('job_id', flat=True)

    # 用job_id找任务点名称
    name_ues = models.TStatCourseJob.objects.filter(job_id__in=jobs)

    name_count = name_ues.values('name').annotate(job_count=Count('job_id')).order_by('-job_count')
    top_names_count = int(name_count.count() * 0.3)

    top_names = name_count[:top_names_count].values_list('name', flat=True)
    # print("需要掌握的任务点名称&&成绩前40%的学生都在学习什么:")
    # print(top_names,"\n")

    #################
    # 找成绩前40~60%的peisonid
    students = models.TStatStudentScore.objects.filter(courseid='222675513').annotate(
        score_float=Cast('score', FloatField())).order_by('-score_float')
    top_students_count1 = int((students.count() / 10) * 4)
    top_students_count2 = int((students.count() / 10) * 6)
    top_students = list(students[top_students_count1 - 1:top_students_count2].values_list('personid', flat=True))

    # 用personid找前50%的job_id
    jobs = models.TStatJobFinish.objects.filter(personid__in=top_students).values_list('job_id', flat=True)

    # 用job_id找任务点名称
    name_ues = models.TStatCourseJob.objects.filter(job_id__in=jobs)

    name_count = name_ues.values('name').annotate(job_count=Count('job_id')).order_by('-job_count')
    top_names_count = int(name_count.count() * 0.3)

    top_names = name_count[:top_names_count].values_list('name', flat=True)
    # print("需要熟悉的任务点名称:")
    # print(top_names,"\n")

    #################
    # 找成绩前40~60%的peisonid
    students = models.TStatStudentScore.objects.filter(courseid='222675513').annotate(
        score_float=Cast('score', FloatField())).order_by('-score_float')
    top_students_count2 = int((students.count() / 10) * 6)
    top_students = list(students[top_students_count2 - 1:].values_list('personid', flat=True))

    # 用personid找前50%的job_id
    jobs = models.TStatJobFinish.objects.filter(personid__in=top_students).values_list('job_id', flat=True)

    # 用job_id找任务点名称
    name_ues = models.TStatCourseJob.objects.filter(job_id__in=jobs)
    name_count = name_ues.values('name').annotate(job_count=Count('job_id')).order_by('-job_count')
    top_names_count = int(name_count.count() * 0.3)

    top_names = name_count[:top_names_count].values_list('name', flat=True)
    # print("需要了解的任务点名称:")
    # print(top_names, "\n")

    #################
    #####总讨论次数,发帖次数,回帖次数
    talk_person_use = models.TStatBbsLog.objects.filter(personid=111946336)
    fatie_count = talk_person_use.annotate(topic_id_int=Cast('topic_id', IntegerField())).filter(topic_id_int__gt=0)
    huitie_count = talk_person_use.annotate(reply_id_int=Cast('reply_id', IntegerField())).filter(reply_id_int__gt=0)
    # print("学生总讨论次数", TStatBbsLog.objects.count())
    # print("学生总发帖次数", TStatBbsLog.objects.annotate(topic_id_int=Cast('topic_id', IntegerField())).filter(topic_id_int__gt=0).count())
    # print("学生总回帖次数", TStatBbsLog.objects.annotate(reply_id_int=Cast('reply_id', IntegerField())).filter(reply_id_int__gt=0).count())
    # print("\n")
    # print("id为111946336学生总讨论次数", talk_person_use.count())
    # print("id为111946336学生总发帖次数", fatie_count.count())
    # print("id为111946336学生总回帖次数", huitie_count.count())
    # print("\n")

    #################
    #####总提交作业数
    work_person_use = models.TStatWorkAnswer.objects.filter(personid=111943630)
    work_person_id = list(work_person_use.values_list('courseid', flat=True))
    fabu_work_person = models.TStatWorkRelation.objects.filter(courseid__in=work_person_id).count()
    # print("课程/总设置作业数",TStatWorkLibrary.objects.count())
    # print("课程/总发布总作业数", TStatWorkRelation.objects.count())
    # print("课程/总共提交作业数", TStatWorkAnswer.objects.count())
    # print("发布给id为111943630学生的作业数为:",fabu_work_person)
    # print("id为111943630学生提交作业数", work_person_use.count())

    #################
    ##求个体课程提交作业率,总提交率
    work_person_use2 = models.TStatWorkAnswer.objects.filter(personid=111943630).filter(courseid=222602451).values(
        'id').distinct().count()
    work_count = models.TStatWorkRelation.objects.filter(courseid=222602451).values('id').distinct().count()
    # print("id为222808035的学生的提交作业率为:%.2f%%" % (work_person_use2/work_count*100))
    # print("id为222808035的学生在id为222602451课程中提交作业率为:%.2f%%" % (work_person_use.count()/fabu_work_person*100))
    # print("\n")

    #################
    #####总提交考试数
    exam_person_use = models.TStatExamAnswer.objects.filter(personid=111944552)
    exam_person_id = list(exam_person_use.values_list('courseid', flat=True))
    fabu_work_person = models.TStatWorkRelation.objects.filter(courseid__in=exam_person_id).count()
    # print("课程/总设置考试数", TStatExamLibrary.objects.count())
    # print("课程/总发布总考试数", TStatExamRelation.objects.count())
    # print("课程/总共提交考试数", TStatExamAnswer.objects.count())
    # print("发布给id为111943630学生的考试数为:",fabu_work_person)
    # print("id为111944552学生提交考试数", exam_person_use.count())
    # exam_person_use2=TStatExamAnswer.objects.filter(personid=111945146).filter(courseid=222820410).values('id').distinct().count()
    # exam_count=TStatExamRelation.objects.filter(courseid=222820410).values('id').distinct().count()
    # print("id为111945146的学生的提交考试率为:%.2f%%" % (exam_person_use.count()/fabu_work_person*100))
    # print("id为111945146的学生在id为222820410课程中提交考试率为:%.2f%%" % (exam_person_use2 / exam_count * 100))
    # print("\n")

    ######一个学生的基本信息
    ##使用20191001037的账号登录学生的personid
    use_personid = models.TStatPerson.objects.filter(login_name=20191001037).values_list('personid', flat=True).first()
    use_name = models.TStatPerson.objects.filter(login_name=20191001037).values_list('user_name', flat=True).first()
    user_course_count = models.TStatCoursePerson.objects.filter(personid=use_personid).values('clazzid').count()
    user_class_count = models.TStatCoursePerson.objects.filter(personid=use_personid).values('clazzid').count()
    print("姓名:", use_name, " 参加的课程数:", user_course_count, " 参加的班级数:", user_class_count)
    # 对于每个课程，获取属于 use_personid 的人的班级数并计算数量
    class_count_by_course = models.TStatCoursePerson.objects.filter(personid=use_personid).values('courseid').annotate(
        class_count=Count('clazzid', distinct=True))
    # 打印每个课程的 class_count
    for item in class_count_by_course:
        print(f"你在课程id为{item['courseid']}的课程中参加了{item['class_count']}个班级。")

    ##活动次数
    # 获取指定 personid 的学生不同 type 的次数
    count_by_type = models.TStatActivityLog.objects.filter(personid=use_personid).values('dtype').annotate(
        count=Count('dtype'))

    # 打印结果
    for item in count_by_type:
        print(f"学生 {use_personid} 有 {item['count']} 条 {item['dtype']} 记录")

    # 获取指定 personid 的学生在不同课程中不同 type 的次数
    count_by_course_and_type = models.TStatActivityLog.objects.filter(personid=use_personid).values('courseid',
                                                                                             'dtype').annotate(
        count=Count('dtype'))

    # 打印结果
    for item in count_by_course_and_type:
        print(f"学生 {use_personid} 在课程 {item['courseid']} 有 {item['count']} 条 {item['dtype']} 记录")


    return render(request, 'component/Portrait.html')
