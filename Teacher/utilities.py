import copy
import json
from django.db.models import *
from django.shortcuts import render
from NewEducation.models import *
from django.db.models import Count
from django.db.models.functions import *
from django.http import JsonResponse
from datetime import datetime, timedelta
from django.db.models import Avg


def index_zzh(request):
    learn_curve = {}

    word_cloud = []

    like_job = []

    hot_act_count = {}

    lesson_act_type = {}

    lesson_act_time = {}

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
    # print(course_all)

    return render(request, 'Teacher/../templates/SuperAdmin/TeachingResult.html', course_all)


def index_lsj(request):
    use_courseid = 224841013
    learn_answer = {}
    bbs_count_day = TStatBbsLog.objects.filter(courseid=use_courseid) \
        .filter(topic_id=0) \
        .annotate(date=TruncDate('last_modify_time')) \
        .values('date') \
        .annotate(count=Count('reply_id')) \
        .order_by('date')
    # print(bbs_count_day)
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
    learn_topic = {}

    for item in bbs_count_days:
        fatie_works = item['count']
        ddaa = str(item['date'])
        learn_topic[ddaa] = fatie_works

    lesson_all = {
        "learn_answer": learn_answer,
        "learn_topic": learn_topic,
    }



    #     with open("data.json", "w") as f:
    #     json.dump(lesson_all, f)

    return render(request, "Teacher/../templates/SuperAdmin/TeachingResult.html", lesson_all)


def index_qjh(request):
    use_courseid = 224841013
    std_personid = 111948612
    use_courseid2 = 222820410   #用于学习成果评估（学生画像，学生课程分析）
    std_personid2 = 111943976    #用于学习成果评估（学生画像，学生课程分析）
    renshu = TStatCoursePerson.objects.filter(courseid=use_courseid).filter(role=3)
    renshu = float(renshu.count())

    lesson_work_post_all_in_all = []

    # 作业完成分布（学生）
    # 改
    # 假设我们的日志记录在 log_date 字段中

    renshu = TStatCoursePerson.objects.filter(courseid=use_courseid).filter(role=3)
    renshu = float(renshu.count())
    lesson_work_post_std = []
    # 所有作业id
    work_library_id = TStatWorkRelation.objects.filter(courseid=use_courseid).values('work_library_id')
    # 所有作业id的数量
    work_count = work_library_id.count()
    for i in range(work_count):
        work_id = work_library_id[i]["work_library_id"]
        work_post = TStatWorkAnswer.objects.filter(courseid=use_courseid) \
            .filter(personid=std_personid) \
            .filter(work_library_id=work_id) \
            .annotate(date=TruncDate('insert_time')) \
            .values('date') \
            .annotate(count_work=Count('id') / renshu) \
            .order_by('date')
        percent_work = 0
        lesson_work_post1 = {}
        for item in work_post:
            percent_work = percent_work + item['count_work']
            percent_work = float("{:.2f}".format(percent_work))
            ddaa = str(item['date'])
            lesson_work_post1[ddaa] = percent_work
        lesson_work_post_std.append(lesson_work_post1)
        lesson_work_post_all_in_all.append(lesson_work_post1)

    # 作业完成分布
    # 改
    lesson_work_post_all = []
    work_library_id = TStatWorkRelation.objects.filter(courseid=use_courseid).values('work_library_id')
    work_count = work_library_id.count()
    for i in range(work_count):
        work_id = work_library_id[i]["work_library_id"]
        work_post = TStatWorkAnswer.objects.filter(courseid=use_courseid) \
            .filter(work_library_id=work_id) \
            .annotate(date=TruncDate('insert_time')) \
            .values('date') \
            .annotate(count_work=Count('id') / renshu) \
            .order_by('date')
        percent_work = 0
        lesson_work_post1 = {}
        for item in work_post:
            percent_work = percent_work + item['count_work']
            percent_work = float("{:.2f}".format(percent_work))
            ddaa = str(item['date'])
            lesson_work_post1[ddaa] = percent_work
        lesson_work_post_all.append(lesson_work_post1)
    #print("*****")
    # print(lesson_work_post_all)
    dict_all = {}

    for dict_one in lesson_work_post_all:
        dict_all = dict(dict_all, **dict_one)
    dict_all = dict(sorted(dict_all.items(), key=lambda d: d[0]))
    # print(f"dict_all{dict(dict_all)}")
    result = []
    for dict_one in lesson_work_post_all:
        flag = 0
        dict_all_copy = dict(copy.deepcopy(dict_all))
        # print(f"@@@@ dict_one:{dict_one}\n@@@@ dict_all_copy:{dict_all_copy}\n")
        for key, value in dict_all_copy.items():
            if key in dict_one:
                dict_all_copy[key] = dict_one[key]
                flag = dict_one[key]
            else:
                dict_all_copy[key] = flag
        result.append(dict_all_copy)




    # 任务点偏好分析
    # 改
    # 任务点种类数

    job_kinds = TStatCourseJob.objects.filter(courseid=use_courseid).values('type').distinct()
    job_kinds_num = job_kinds.count()
    job_like = TStatCourseJob.objects.select_related(' TStatJobFinish').filter(courseid=use_courseid).values(
        'type').annotate(count=Count('type'))

    lesson_job_like = {

    }
    for item in job_like:
        lesson_job_like[item["type"]] = item["count"]

    # 学习成果评估（学生个人成绩与课程平均成绩）
    # 学生.学生画像   学生.课程分析
    s1 = 0  # 90-100
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0  # 0-60
    score_sum = 0
    renshu2 = int(renshu)
    std_grade_std = TStatExamAnswer.objects.filter(courseid=use_courseid2).filter(personid=std_personid2).values('score')
    # 学生个人成绩
    print("*******")
    print(std_grade_std)
    std_final_score_std = {

    }


    std_grade = TStatExamAnswer.objects.filter(courseid=use_courseid2).values('score')
    for i in range(renshu2):
        rr = float(std_grade[i]['score'])
        score_sum = score_sum + rr
        if rr < 60:
            s5 = s5 + 1
        elif 60 <= rr and rr < 70:
            s4 = s4 + 1
        elif 70 <= rr and rr < 80:
            s3 = s3 + 1
        elif 80 <= rr and rr < 90:
            s2 = s2 + 1
        elif 90 <= rr and rr < 100:
            s1 = s1 + 1
    average = score_sum / renshu
    average = float("{:.2f}".format(average))
    #课程平均成绩
    std_final_score = {

    }
    std_final_score["average"] = average
    std_final_score["90-100"] = s1
    std_final_score["80-90"] = s2
    std_final_score["70-80"] = s3
    std_final_score["60-70"] = s4
    std_final_score["0-60"] = s5










    # 总体成绩分析
    # 改
    std_grade = TStatStudentScore.objects.filter(courseid=use_courseid).values('score')

    s1 = 0  # 90-100
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0  # 0-60
    score_sum = 0
    renshu2 = int(renshu)

    for i in range(renshu2):
        rr = float(std_grade[i]['score'])
        score_sum = score_sum + rr
        if rr < 60:
            s5 = s5 + 1
        elif 60 <= rr and rr < 70:
            s4 = s4 + 1
        elif 70 <= rr and rr < 80:
            s3 = s3 + 1
        elif 80 <= rr and rr < 90:
            s2 = s2 + 1
        elif 90 <= rr and rr < 100:
            s1 = s1 + 1
    average = score_sum / renshu
    average = float("{:.2f}".format(average))
    std_final_score = {

    }
    std_final_score["average"] = average
    std_final_score["90-100"] = s1
    std_final_score["80-90"] = s2
    std_final_score["70-80"] = s3
    std_final_score["60-70"] = s4
    std_final_score["0-60"] = s5

    # 考试质量分析
    use_courseid2 = 222820410
    std_exam_id = TStatExamRelation.objects.filter(courseid=use_courseid2).values('exam_id')

    std_exam_score_nan_du = {

    }
    # 考试门数
    exam_count = TStatExamRelation.objects.filter(courseid=use_courseid2).values('exam_id').count()
    # 各门考试平均分
    exam_avg = TStatExamAnswer.objects.filter(courseid=use_courseid2).values('exam_id').annotate(
        score_avg=Avg("score")).values('exam_id', 'score_avg')
    # 成绩平均分
    std_grade2 = TStatStudentScore.objects.filter(courseid=use_courseid2).values('score')
    score_sum = 0
    renshu3 = int(renshu)
    for i in range(renshu3):
        rr = float(std_grade2[i]['score'])
        score_sum = score_sum + rr
    # 期末平均分
    final_average = score_sum / renshu
    final_average = final_average / 100
    final_average = float("{:.2f}".format(final_average))

    for i in range(work_count):
        work_id = work_library_id[i]["work_library_id"]
        work_post = TStatWorkAnswer.objects.filter(courseid=use_courseid) \
            .filter(work_library_id=work_id) \
            .annotate(date=TruncDate('insert_time')) \
            .values('date') \
            .annotate(count_work=Count('id') / renshu) \
            .order_by('date')
        percent_work = 0
        lesson_work_post1 = {}
        for item in work_post:
            percent_work = percent_work + item['count_work']
            percent_work = float("{:.2f}".format(percent_work))
            ddaa = str(item['date'])
            lesson_work_post1[ddaa] = percent_work

    std_exam_score_nan_du["avg_score"] = final_average
    for item in range(exam_count):
        ff = float(exam_avg[item]['score_avg'])
        ff = ff / 100
        ff = float("{:.2f}".format(ff))
        std_exam_score_nan_du[exam_avg[item]['exam_id']] = ff

    # 教师任务点完成分布：*******(return job_finish_all)
    # 改
    # 任务点总数
    job_total = TStatCourseJob.objects.filter(courseid=use_courseid)
    job_total = float(job_total.count())
    # 应完成人次
    job_should_finish = float(job_total) * renshu

    # 已完成人次
    job_finish = TStatJobFinish.objects.filter(courseid=use_courseid).filter(personid=std_personid)
    job_finish = float(job_finish.count())

    job_finish_all = {
        "job_total": job_total,
        "job_should_finish": job_should_finish,  # 应完成人次
        "job_finish": job_finish  # 已完成人次
    }

    # 学生个人任务点完成分布：*******(return job_finish_all)
    #
    # 任务点总数
    job_total = TStatCourseJob.objects.filter(courseid=use_courseid)
    job_total = float(job_total.count())
    # 应完成人次
    job_should_finish = float(job_total)

    # 给定学生的完成数量
    job_test_std = TStatJobFinish.objects.filter(courseid=use_courseid).filter(personid=std_personid)
    test_std_finish = job_test_std.count()
    # 每个学生的完成数量
    job_std = TStatJobFinish.objects.filter(courseid=use_courseid).values('personid').annotate(
        count=Count('personid')).order_by('personid')

    ssum = job_std.count()
    num1 = 0
    for item in job_std:
        if test_std_finish > item['count']:
            num1 = num1 + 1

    job_chao_guo = 1.0 * num1 / renshu

    job_finish_std = {
        "job_total": job_total,  # 任务点总数
        "job_finish": test_std_finish,  # 给定学生的完成数量数量
        "job_chao_guo": job_chao_guo  # 任务点完成率超过了job_chao_guo%的人
    }

    learn_answer = {

    }
    bbs_count_day = TStatBbsLog.objects.filter(courseid=use_courseid) \
        .filter(topic_id=0) \
        .annotate(date=TruncDate('last_modify_time')) \
        .values('date') \
        .annotate(count=Count('reply_id')) \
        .order_by('date')

    for item in bbs_count_day:
        huitie_work = item['count']
        ddaa = str(item['date'])
        learn_answer[ddaa] = huitie_work

    lesson_all = {

        "lesson_work_post_all_in_all": lesson_work_post_all_in_all,  # 这个是报错的
        #"lesson_work_post": lesson_work_post_all,  # 作业完成分布作业1 ￥
        "lesson_work_post": result,  # 作业完成分布作业1 ￥
        "job_finish_all": job_finish_all,  # 任务点完成分布 ￥
        "lesson_job_like": lesson_job_like,  # 任务点偏好 ￥
        "std_final_score": std_final_score,  # 总体成绩分析  ￥
        "std_exam_score_nan_du": std_exam_score_nan_du,  # 考试质量分析
    }

    # ***************提交时注释掉
    with open("data.json", "w") as f:
        json.dump(lesson_all, f)

    return render(request, "Teacher/../templates/SuperAdmin/TeachingResult.html", lesson_all)
