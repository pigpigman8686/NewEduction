# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TStatActivityLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    dtype = models.CharField(max_length=30, blank=True, null=True)
    activity_id = models.CharField(max_length=100, blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    attend_id = models.CharField(max_length=100, blank=True, null=True)
    attend_time = models.DateTimeField(blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_activity_log'


class TStatBbsLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    bbs_id = models.CharField(max_length=100, blank=True, null=True)
    topic_id = models.CharField(max_length=50, blank=True, null=True)
    parent_id = models.CharField(max_length=50, blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    reply_id = models.CharField(max_length=50, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_bbs_log'


class TStatClazz(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    clazz_number = models.CharField(max_length=100, blank=True, null=True)
    student_count = models.IntegerField(blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    semester = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_clazz'


class TStatCourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    chapter_count = models.CharField(max_length=255, blank=True, null=True)
    course_number = models.CharField(max_length=255, blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    group_name = models.CharField(max_length=255, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_course'


class TStatCourseData(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    ptype = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    url = models.CharField(max_length=255, blank=True, null=True)
    size = models.CharField(max_length=255, blank=True, null=True)
    object_id = models.CharField(max_length=255, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
    data_id = models.CharField(max_length=255, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_course_data'


class TStatCourseJob(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    job_id = models.CharField(max_length=255, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_course_job'


class TStatCoursePerson(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
    role = models.IntegerField(blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_course_person'


class TStatExamAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    work_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    answer_time = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    piyue_person_id = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    piyue_time = models.CharField(max_length=255, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
    fid = models.BigIntegerField(blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    answerid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_exam_answer'


class TStatExamLibrary(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
    paper_library_id = models.CharField(max_length=255, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_exam_library'


class TStatExamRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.CharField(max_length=255, blank=True, null=True)
    end_time = models.CharField(max_length=255, blank=True, null=True)
    specified_time = models.CharField(max_length=255, blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
    exam_id = models.CharField(max_length=255, blank=True, null=True)
    paper_library_id = models.CharField(max_length=255, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_exam_relation'


class TStatJobFinish(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    job_id = models.CharField(max_length=255, blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_job_finish'


class TStatLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    ptype = models.CharField(max_length=255, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_log'


class TStatOnlinePerson(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    ip = models.CharField(max_length=100, blank=True, null=True)
    prole = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_online_person'


class TStatOnlineTime(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    online_time = models.DateTimeField(blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_online_time'


class TStatPerson(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=255, blank=True, null=True)
    login_name = models.CharField(max_length=255, blank=True, null=True)
    role = models.IntegerField(blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_person'


class TStatQuestionBank(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
    question_id = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=30, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_question_bank'


class TStatStudentScore(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_student_score'


class TStatWidgetLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    dtype = models.CharField(max_length=30, blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    activity_id = models.CharField(max_length=100, blank=True, null=True)
    attend_count = models.CharField(max_length=255, blank=True, null=True)
    send_to_student = models.CharField(max_length=255, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_widget_log'


class TStatWorkAnswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    work_id = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    answer_time = models.CharField(max_length=255, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    piyue_person_id = models.CharField(max_length=255, blank=True, null=True)
    ip = models.CharField(max_length=32, blank=True, null=True)
    piyue_time = models.CharField(max_length=255, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
    fid = models.BigIntegerField(blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    answerid = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_work_answer'


class TStatWorkLibrary(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
    paper_library_id = models.CharField(max_length=255, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_work_library'


class TStatWorkRelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    insert_time = models.DateTimeField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    last_modify_time = models.DateTimeField(blank=True, null=True)
    personid = models.CharField(max_length=100, blank=True, null=True)
    courseid = models.CharField(max_length=100, blank=True, null=True)
    score = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.CharField(max_length=100, blank=True, null=True)
    end_time = models.CharField(max_length=100, blank=True, null=True)
    specified_time = models.CharField(max_length=100, blank=True, null=True)
    clazzid = models.CharField(max_length=100, blank=True, null=True)
    isdeleted = models.IntegerField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
    work_id = models.CharField(max_length=255, blank=True, null=True)
    work_library_id = models.CharField(max_length=255, blank=True, null=True)
    fid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_stat_work_relation'
