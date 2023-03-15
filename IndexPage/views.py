from django.shortcuts import render, redirect
from IndexPage import models

from django.db.models import Count, F
from .models import *
from django.db.models import FloatField, Avg, Q

from django.db.models import IntegerField, Value
from django.db.models.functions import Cast
import pandas as pd

def learningstyle_style(request):
    ##学习风格-学习方式
    use_personid = 147374889
    for item in TStatCourseJob.objects.filter(personid=use_personid).values('type').annotate(count=Count('type')):
        print(f"学生 {use_personid} 有 {item['count']} 条 {item['type']} 记录");
    studystyle_most=TStatCourseJob.objects.filter(personid=use_personid).values('type').annotate(count=Count('type')).order_by('-count').first();
    print(f"学生 {use_personid} 的学习方式偏好分类: {studystyle_most['type']}型 一共学习了 {studystyle_most['count']} 次")


    #作业完成率              ##待修改:求每门课程的作业完成率
    work_person_use=TStatWorkAnswer.objects.filter(personid=111943630)
    work_person_id= list(work_person_use.values_list('courseid',flat=True))
    fabu_work_person=TStatWorkRelation.objects.filter(courseid__in=work_person_id).count()
    work_person_use2=TStatWorkAnswer.objects.filter(personid=111943630).filter(courseid=222602451).values('id').count()
    work_count=TStatWorkRelation.objects.filter(courseid=222602451).values('id').count()
    print("id为222808035的学生的提交作业率为:%.2f%%" % (work_person_use2/work_count*100))
    print("id为222808035的学生在id为222602451课程中提交作业率为:%.2f%%" % (work_person_use.count()/fabu_work_person*100))
    print("\n")

    ##作业正确率
    use_personid = 111945078
    #不同课程平均成绩
    avg_score = TStatWorkAnswer.objects.filter(
        personid=use_personid
    ).values('courseid').annotate(avg_score=Avg('score'))
    for item in avg_score:
        print(f"{use_personid} 学生在 {item['courseid']}为id的课程 中的作业正确率为 {item['avg_score']:.2f}%")

    #总平均成绩
    total_avg_score = TStatWorkAnswer.objects.filter(
        personid=use_personid
    ).aggregate(avg_score=Avg('score'))
    print(f"{use_personid} 学生的总作业正确率为 {total_avg_score['avg_score']:.2f}%")

    ##不同课程给次数
    personid_id = 147385772
    course_id = 222820410

    count_by_type = TStatActivityLog.objects.filter(personid=personid_id,courseid=course_id ).values('dtype').annotate(count=Count('dtype'))
    count_by_type_total = TStatActivityLog.objects.filter(courseid=course_id).values('dtype').annotate(count=Count('dtype'))
    count_by_type_rate = Type_Rate.objects.values('dtype')
    # # 遍历第一个查询集，找到相同的dtype，并计算百分比
    # for item in count_by_type:
    #     dtype = item['dtype']
    #     count = item['count']
    #     total = count_by_type_total.get(dtype=dtype)['count']
    #     rate = (count / total) * 100
    #     # 把结果添加到第三个查询集中
    #     count_by_type_rate.
    # print(count_by_type_rate)

    #####总提交作业数
    work_person_use = TStatWorkAnswer.objects.filter(personid=111943630)
    work_person_id = list(work_person_use.values_list('courseid', flat=True))
    fabu_work_person1 = TStatWorkRelation.objects.filter(courseid__in=work_person_id)
    print("课程/总设置作业数", TStatWorkLibrary.objects.count())
    print("课程/总发布总作业数", TStatWorkRelation.objects.count())
    print("课程/总共提交作业数", TStatWorkAnswer.objects.count())
    print("发布给id为111943630学生的作业数为:", fabu_work_person1.count())
    print("id为111943630学生提交作业数", work_person_use.count())

    #################
    ##求个体课程提交作业率,总提交率
    work_person_use2 = TStatWorkAnswer.objects.filter(personid=111943630).filter(courseid=222602451)
    fabu_work_person2 = TStatWorkRelation.objects.filter(courseid=222602451)
    print("id为222808035的学生的提交作业率为:%.2f%%" % (work_person_use.count() / fabu_work_person1.count() * 100))
    print("id为222808035的学生在id为222602451课程中提交作业率为:%.2f%%" % (
                work_person_use2.count() / fabu_work_person2.count() * 100))
    print("\n")

    #################
    #####总提交考试数
    exam_person_use = TStatExamAnswer.objects.filter(personid=111944552)
    exam_person_id = list(exam_person_use.values_list('courseid', flat=True))
    fabu_exam_person1 = TStatExamRelation.objects.filter(courseid__in=exam_person_id)
    print("课程/总设置考试数", TStatExamLibrary.objects.count())
    print("课程/总发布总考试数", TStatExamRelation.objects.count())
    print("课程/总共提交考试数", TStatExamAnswer.objects.count())
    print("发布给id为111943630学生的考试数为:", fabu_work_person1.count())
    print("id为111943630学生提交考试数", exam_person_use.count())

    ##求个体课程提交考试率,总考试率
    exam_person_use2 = TStatExamAnswer.objects.filter(personid=111944552, courseid=222820410)
    fabu_exam_person2 = TStatExamRelation.objects.filter(courseid=222820410)
    print("id为222808035的学生的提交考试率为:%.2f%%" % (exam_person_use.count() / fabu_exam_person1.count() * 100))
    print("id为222808035的学生在id为222602451课程中提交考试率为:%.2f%%" % (exam_person_use2.count() / fabu_exam_person2.count() * 100))
    print("\n")









    return render(request, 'index.html')










def index(request):
    # #################
    # #找成绩前40%的peisonid
    # students = TStatStudentScore.objects.filter(courseid='222675513').annotate(score_float=Cast('score', FloatField())).order_by('-score_float')
    # top_students_count = int((students.count() / 10)*4)
    # top_students=list(students[:top_students_count].values_list('personid', flat=True))
    #
    # #用personid找前50%的job_id
    # jobs = TStatJobFinish.objects.filter(personid__in=top_students).values_list('job_id', flat=True)
    #
    # #用job_id找任务点名称
    # name_ues=TStatCourseJob.objects.filter(job_id__in=jobs)
    #
    # name_count = name_ues.values('name').annotate(job_count=Count('job_id')).order_by('-job_count')
    # top_names_count = int(name_count.count() * 0.3)
    #
    #
    # top_names = name_count[:top_names_count].values_list('name', flat=True)
    # print("需要掌握的任务点名称&&成绩前40%的学生都在学习什么:")
    # print(top_names,"\n")
    #
    #
    # #################
    # # 找成绩前40~60%的peisonid
    # students = TStatStudentScore.objects.filter(courseid='222675513').annotate(
    #     score_float=Cast('score', FloatField())).order_by('-score_float')
    # top_students_count1 = int((students.count() / 10) * 4)
    # top_students_count2 = int((students.count() / 10) * 6)
    # top_students = list(students[top_students_count1-1:top_students_count2 ].values_list('personid', flat=True))
    #
    # # 用personid找前50%的job_id
    # jobs = TStatJobFinish.objects.filter(personid__in=top_students).values_list('job_id', flat=True)
    #
    # # 用job_id找任务点名称
    # name_ues = TStatCourseJob.objects.filter(job_id__in=jobs)
    #
    # name_count = name_ues.values('name').annotate(job_count=Count('job_id')).order_by('-job_count')
    # top_names_count = int(name_count.count() * 0.3)
    #
    # top_names = name_count[:top_names_count].values_list('name', flat=True)
    # print("需要熟悉的任务点名称:")
    # print(top_names,"\n")
    #
    # #################
    # # 找成绩前40~60%的peisonid
    # students = TStatStudentScore.objects.filter(courseid='222675513').annotate(
    #     score_float=Cast('score', FloatField())).order_by('-score_float')
    # top_students_count2 = int((students.count() / 10) * 6)
    # top_students = list(students[top_students_count2-1:].values_list('personid', flat=True))
    #
    # # 用personid找前50%的job_id
    # jobs = TStatJobFinish.objects.filter(personid__in=top_students).values_list('job_id', flat=True)
    #
    # # 用job_id找任务点名称
    # name_ues = TStatCourseJob.objects.filter(job_id__in=jobs)
    # name_count = name_ues.values('name').annotate(job_count=Count('job_id')).order_by('-job_count')
    # top_names_count = int(name_count.count() * 0.3)
    #
    # top_names = name_count[:top_names_count].values_list('name', flat=True)
    # print("需要了解的任务点名称:")
    # print(top_names, "\n")
    #
    #
    # #################
    # #####总讨论次数,发帖次数,回帖次数
    # talk_person_use = TStatBbsLog.objects.filter(personid=111946336)
    # fatie_count = talk_person_use.annotate(topic_id_int=Cast('topic_id', IntegerField())).filter(topic_id_int__gt=0)
    # huitie_count = talk_person_use.annotate(reply_id_int=Cast('reply_id', IntegerField())).filter(reply_id_int__gt=0)
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
    work_person_use=TStatWorkAnswer.objects.filter(personid=111943630)
    work_person_id= list(work_person_use.values_list('courseid',flat=True))
    fabu_work_person1=TStatWorkRelation.objects.filter(courseid__in=work_person_id)
    print("课程/总设置作业数",TStatWorkLibrary.objects.count())
    print("课程/总发布总作业数", TStatWorkRelation.objects.count())
    print("课程/总共提交作业数", TStatWorkAnswer.objects.count())
    print("发布给id为111943630学生的作业数为:",fabu_work_person1.count())
    print("id为111943630学生提交作业数", work_person_use.count())


    #################
    ##求个体课程提交作业率,总提交率
    work_person_use2=TStatWorkAnswer.objects.filter(personid=111943630).filter(courseid=222602451)
    fabu_work_person2=TStatWorkRelation.objects.filter(courseid=222602451)
    print("id为222808035的学生的提交作业率为:%.2f%%" % (work_person_use.count()/fabu_work_person1.count()*100))
    print("id为222808035的学生在id为222602451课程中提交作业率为:%.2f%%" % (work_person_use2.count()/fabu_work_person2.count()*100))
    print("\n")



    #################
    #####总提交考试数
    exam_person_use = TStatExamAnswer.objects.filter(personid=111944552)
    exam_person_id = list(exam_person_use.values_list('courseid', flat=True))
    fabu_exam_person1 = TStatExamRelation.objects.filter(courseid__in=exam_person_id)
    print("课程/总设置考试数", TStatExamLibrary.objects.count())
    print("课程/总发布总考试数", TStatExamRelation.objects.count())
    print("课程/总共提交考试数", TStatExamAnswer.objects.count())
    print("发布给id为111943630学生的考试数为:",fabu_work_person1.count())
    print("id为111943630学生提交考试数", exam_person_use.count())

    ##求个体课程提交考试率,总考试率
    exam_person_use2 = TStatExamAnswer.objects.filter(personid=111944552, courseid=222820410)
    fabu_exam_person2 = TStatExamRelation.objects.filter(courseid=222820410)
    print("id为222808035的学生的提交考试率为:%.2f%%" % (exam_person_use.count() / fabu_exam_person1.count() * 100))
    print("id为222808035的学生在id为222602451课程中提交考试率为:%.2f%%" % (exam_person_use2.count() / fabu_exam_person2.count() * 100))
    print("\n")



    #
    # ######一个学生的基本信息
    # ##使用20191001037的账号登录学生的personid
    # use_personid = TStatPerson.objects.filter(login_name=20191001037).values_list('personid', flat=True).first()
    # use_name=TStatPerson.objects.filter(login_name=20191001037).values_list('user_name',flat=True).first()
    # user_course_count=TStatCoursePerson.objects.filter(personid=use_personid).values('clazzid').count()
    # user_class_count=TStatCoursePerson.objects.filter(personid=use_personid).values('clazzid').count()
    # print("姓名:", use_name, " 参加的课程数:", user_course_count, " 参加的班级数:", user_class_count)
    # # 对于每个课程，获取属于 use_personid 的人的班级数并计算数量
    # class_count_by_course = TStatCoursePerson.objects.filter(personid=use_personid).values('courseid').annotate(class_count=Count('clazzid', distinct=True))
    # # 打印每个课程的 class_count
    # for item in class_count_by_course:
    #     print(f"你在课程id为{item['courseid']}的课程中参加了{item['class_count']}个班级。")
    #
    # ##活动次数
    # # 获取指定 personid 的学生不同 type 的次数
    # count_by_type = TStatActivityLog.objects.filter(personid=use_personid).values('dtype').annotate( count=Count('dtype'))
    #
    # # 打印结果
    # for item in count_by_type:
    #     print(f"学生 {use_personid} 有 {item['count']} 条 {item['dtype']} 记录")
    #
    # ##待修改,需要考虑班级
    # # 获取指定 personid 的学生在不同课程中不同 type 的次数
    # count_by_course_and_type = TStatActivityLog.objects.filter(personid=use_personid).values('courseid', 'dtype').annotate(count=Count('dtype'))
    #
    # # 打印结果
    # for item in count_by_course_and_type:
    #     print(f"学生 {use_personid} 在课程 {item['courseid']} 有 {item['count']} 条 {item['dtype']} 记录")


    return render(request, 'index.html')



def get_data(request):
    obj = models.TStatWorkRelation.objects.filter(id=1).first()
    print(obj.id)
    return render(request, 'index.html', {'row': obj})
