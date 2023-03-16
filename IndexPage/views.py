from django.shortcuts import render, redirect
from IndexPage import models

from django.db.models import Count, F
from .models import *
from django.db.models import FloatField, Avg, Q

from django.db.models import IntegerField, Value
from django.db.models.functions import Cast
import pandas as pd

def learningstyle_style(request):
    ##学习风格
    use_personid = 147374889
    for item in TStatCourseJob.objects.filter(personid=use_personid).values('type').annotate(count=Count('type')):
        print(f"学生 {use_personid} 有 {item['count']} 条 {item['type']} 记录");
    studystyle_most=TStatCourseJob.objects.filter(personid=use_personid).values('type').annotate(count=Count('type')).order_by('-count').first();
    print(f"学生 {use_personid} 的学习方式偏好分类: {studystyle_most['type']}型 一共学习了 {studystyle_most['count']} 次")
    print()

    #作业完成率              ##待修改:求每门课程的作业完成率
    use_personid = 111943630
    use_courseid = 222602451
    work_person_use=TStatWorkAnswer.objects.filter(personid=use_personid)
    work_person_id= list(work_person_use.values_list('courseid', flat=True))
    fabu_work_person=TStatWorkRelation.objects.filter(courseid__in=work_person_id)
    work_person_use2=TStatWorkAnswer.objects.filter(personid=use_personid).filter(courseid=use_courseid).values('id')
    fabu_work_person2 = TStatWorkRelation.objects.filter(courseid=use_courseid)
    print("id为222808035的学生的提交作业率为:%.2f%%" % (work_person_use.count()/fabu_work_person.count()*100))
    print("id为222808035的学生在id为222602451课程中提交作业率为:%.2f%%" % (work_person_use2.count()/fabu_work_person2.count()*100))
    print()

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
    print()


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
    print("id为222808035的学生在id为222602451课程中提交作业率为:%.2f%%" % (work_person_use2.count() / fabu_work_person2.count() * 100))
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

    ##对不同任务点名称的兴趣
    use_personid=111943630
    job_like_id=TStatJobFinish.objects.filter(personid=use_personid).values('job_id').annotate(count=Count('job_id')).order_by('-count').all()[:3]
    print("学生最感兴趣的任务:")
    for item in job_like_id:
        job_like_name=TStatCourseJob.objects.filter(job_id=item['job_id']).values('name').first()
        print(job_like_name['name'])
    print()

    #####总讨论次数,发帖次数,回帖次数
    use_personid=111946336
    use_courseid=224841013
    talk_person_use = TStatBbsLog.objects.filter(personid=use_personid)
    fatie_count = talk_person_use.annotate(topic_id_int=Cast('topic_id', IntegerField())).filter(topic_id_int__gt=0)
    huitie_count = talk_person_use.annotate(reply_id_int=Cast('reply_id', IntegerField())).filter(reply_id_int__gt=0)
    print("学生总讨论次数", TStatBbsLog.objects.count())
    print("学生总发帖次数", TStatBbsLog.objects.annotate(topic_id_int=Cast('topic_id', IntegerField())).filter(topic_id_int__gt=0).count())
    print("学生总回帖次数", TStatBbsLog.objects.annotate(reply_id_int=Cast('reply_id', IntegerField())).filter(reply_id_int__gt=0).count())
    print("id为111946336学生总讨论次数", talk_person_use.count())
    print("id为111946336学生总发帖次数", fatie_count.count())
    print("id为111946336学生总回帖次数", huitie_count.count())
    print("\n")
    personid_course=list(TStatBbsLog.objects.filter(personid=use_personid).values_list('courseid',flat=True))
    talk_course_use1=TStatBbsLog.objects.filter(courseid=use_courseid)
    talk_course_use2=TStatBbsLog.objects.filter(courseid__in=personid_course)
    talk_person_count1=TStatBbsLog.objects.filter(personid=use_personid,courseid=use_courseid)
    talk_person_count2=TStatBbsLog.objects.filter(courseid__in=personid_course,personid=use_personid)
    talk_rate=talk_person_count1.count()/talk_course_use1.count()*100
    talk_rate_total= talk_person_count2.count() / talk_course_use2.count() * 100
    print(f"id 为 {use_personid} 的学生在 {use_courseid} 课程中讨论率为 {talk_rate:.2f}%")
    print(f"id 为 {use_personid} 的学生的总讨论率为 {talk_rate_total:.2f}%")
    fatie_course_use1 = TStatBbsLog.objects.filter(courseid=use_courseid).annotate(topic_id_int=Cast('topic_id', IntegerField())).filter(topic_id_int__gt=0)
    fatie_course_use2 = TStatBbsLog.objects.filter(courseid__in=personid_course).annotate(topic_id_int=Cast('topic_id', IntegerField())).filter(topic_id_int__gt=0)
    fatie_person_count1 = TStatBbsLog.objects.filter(personid=use_personid, courseid=use_courseid).annotate(topic_id_int=Cast('topic_id', IntegerField())).filter(topic_id_int__gt=0)
    fatie_person_count2 = TStatBbsLog.objects.filter(personid=use_personid, courseid__in=personid_course).annotate(topic_id_int=Cast('topic_id', IntegerField())).filter(topic_id_int__gt=0)
    fatie_rate = fatie_person_count1.count() / fatie_course_use1.count() * 100
    fatie_rate_total = fatie_person_count2.count() / fatie_course_use2.count() * 100
    print(f"id 为 {use_personid} 的学生在 {use_courseid} 课程中发帖率为 {fatie_rate:.2f}%")
    print(f"id 为 {use_personid} 的学生的总发帖率为 {fatie_rate_total:.2f}%")
    huitie_course_use1 = TStatBbsLog.objects.filter(courseid=use_courseid).annotate(reply_id_int=Cast('reply_id', IntegerField())).filter(reply_id_int__gt=0)
    huitie_course_use2 = TStatBbsLog.objects.filter(courseid__in=personid_course).annotate(reply_id_int=Cast('reply_id', IntegerField())).filter(reply_id_int__gt=0)
    huitie_person_count1 = TStatBbsLog.objects.filter(personid=use_personid, courseid=use_courseid).annotate(reply_id_int=Cast('reply_id', IntegerField())).filter(reply_id_int__gt=0)
    huitie_person_count2 = TStatBbsLog.objects.filter(personid=use_personid, courseid__in=personid_course).annotate(reply_id_int=Cast('reply_id', IntegerField())).filter(reply_id_int__gt=0)
    huitie_rate = huitie_person_count1.count() / huitie_course_use1.count() * 100
    huitie_rate_total = huitie_person_count2.count() / huitie_course_use2.count() * 100
    print(f"id 为 {use_personid} 的学生在 {use_courseid} 课程中回帖率为 {huitie_rate:.2f}%")
    print(f"id 为 {use_personid} 的学生的总回帖率为 {huitie_rate_total:.2f}%")
    print("\n")

    ##获取指定 personid 的学生不同 type 的次数
    use_personid=111946336
    use_courseid=224841013
    person_course=list(TStatActivityLog.objects.filter(personid=use_personid).values_list('courseid',flat=True))
    count_by_type = TStatActivityLog.objects.filter(personid=use_personid).values('dtype').annotate(count=Count('dtype'))

    # 学生总的各活动次数
    for item in count_by_type:
        print(f"学生 {use_personid} 有 {item['count']} 条 {item['dtype']} 记录")

    # 获取指定 personid 的学生在不同课程中不同 type 的次数
    count_by_course_and_type = TStatActivityLog.objects.filter(personid=use_personid).values('courseid', 'dtype').annotate(count=Count('dtype'))
    count_by_type_total=TStatActivityLog.objects.filter(courseid=use_courseid).values('dtype').annotate(count=Count('dtype'))
    count_by_type_total2=TStatActivityLog.objects.filter(courseid__in=person_course).values('dtype').annotate(count=Count('dtype'))

    # 打印结果
    for item in count_by_course_and_type:
        dtype = item['dtype']
        count=item['count']
        total = count_by_type_total.get(dtype=dtype)['count']
        total2 = count_by_type_total2.get(dtype=dtype)['count']
        rate = (count / total) * 100
        count2= count_by_type.get(dtype=dtype)['count']
        rate2=(count2 / total2) * 100
        print(f"学生 {use_personid} 在课程 {item['courseid']} 有 {item['count']} 条 {item['dtype']} 记录")
        print(f"该学生在课程 {use_courseid}中  活动 {item['dtype']} 比例为 %.2f%%" % rate)
        print(f"该学生活动 {item['dtype']} 总比例为 %.2f%%" % rate2)






    return render(request, 'index.html')










def index(request):
    #################
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
    print("需要掌握的任务点名称&&成绩前40%的学生都在学习什么:")
    print(top_names,"\n")


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
    print("需要熟悉的任务点名称:")
    print(top_names,"\n")

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
    print("需要了解的任务点名称:")
    print(top_names, "\n")


    #################
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
