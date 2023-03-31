from django.shortcuts import render

# Create your views here.


def analyse(request):
    message = {
        "lesson_work_post_all_in_all": [
            {
                "2022-05-17": 0.19,
                "2022-05-18": 0.45,
                "2022-05-19": 0.49,
                "2022-05-20": 0.53,
                "2022-05-23": 0.6,
                "2022-05-29": 0.64,
                "2022-06-01": 0.71,
                "2022-06-07": 0.75,
                "2022-06-08": 0.82,
                "2022-06-09": 0.86,
                "2022-06-11": 0.93,
                "2022-06-12": 1.0
            },
            {
                "2022-05-30": 0.96,
                "2022-06-01": 1.0
            }
        ],
        "lesson_work_post": [
            {
                "2022-05-17": 0.19,
                "2022-05-18": 0.45,
                "2022-05-19": 0.49,
                "2022-05-20": 0.53,
                "2022-05-23": 0.6,
                "2022-05-29": 0.64,
                "2022-05-30": 0.64,
                "2022-06-01": 0.71,
                "2022-06-07": 0.75,
                "2022-06-08": 0.82,
                "2022-06-09": 0.86,
                "2022-06-11": 0.93,
                "2022-06-12": 1.0
            },
            {
                "2022-05-17": 0,
                "2022-05-18": 0,
                "2022-05-19": 0,
                "2022-05-20": 0,
                "2022-05-23": 0,
                "2022-05-29": 0,
                "2022-05-30": 0.96,
                "2022-06-01": 1.0,
                "2022-06-07": 1.0,
                "2022-06-08": 1.0,
                "2022-06-09": 1.0,
                "2022-06-11": 1.0,
                "2022-06-12": 1.0
            }
        ],
        "job_finish_all": {
            "job_total": 1.0,
            "job_should_finish": 27.0,
            "job_finish": 0.0
        },
        "lesson_job_like": {
            "WorkAttachment": 1,
            "VideoAttachment": 0
        },
        "std_final_score": {
            "average": 46.19,
            "90-100": 0,
            "80-90": 0,
            "70-80": 0,
            "60-70": 0,
            "0-60": 27
        },
        "std_exam_score_nan_du": {
            "avg_score": 0.53,
            "1830642": 0.89,
            "1861569": 0.89,
            "1924004": 0.94,
            "1924007": 0.94,
            "2002366": 0.96
        },
        "learn_answer": {
            "2022-05-11": 8,
            "2022-06-15": 250,
            "2022-06-17": 6,
            "2022-06-18": 4,
            "2022-06-19": 14,
            "2022-06-20": 8,
            "2022-06-22": 32
        },
        "learn_topic": {
            "2022-05-11": 2,
            "2022-06-15": 54
        },
        "use_courseid": 224841013,
        "lesson_act_time": {
            "4": 114,
            "5": 168,
            "6": 76
        },
        "lesson_act_type": {
            "VoteLog": 51,
            "WorkLog": 234,
            "PreampAnswerLog": 38,
            "ChooseSomeoneLog": 8,
            "TaskLog": 27
        },
        "hot_act_count": {
            "3": [
                0,
                0,
                23,
                57,
                92,
                53
            ],
            "4": [
                6,
                0,
                20,
                54,
                82,
                74
            ],
            "5": [
                28,
                14,
                127,
                157,
                225,
                250
            ]
        },
        "like_job": [
            {
                "name": "\u7b2c\u4e00\u7ae0\u5c0f\u6d4b\u9a8c",
                "count": 33
            },
            {
                "name": "SP1-1\u90e8\u5206.mp4",
                "count": 33
            },
            {
                "name": "sp1-2\u90e8\u5206.mp4",
                "count": 28
            },
            {
                "name": "\u7b2c\u4e8c\u7ae0\u5c0f\u6d4b\u9a8c",
                "count": 23
            },
            {
                "name": "sp2-1.mp4",
                "count": 18
            }
        ],
        "word_cloud": [
            {
                "name": "\u7b2c\u4e00\u7ae0\u5c0f\u6d4b\u9a8c",
                "count": 1
            },
            {
                "name": "SP1-1\u90e8\u5206.mp4",
                "count": 1
            },
            {
                "name": "sp1-2\u90e8\u5206.mp4",
                "count": 1
            },
            {
                "name": "sp2-1.mp4",
                "count": 1
            },
            {
                "name": "\u7b2c\u4e8c\u7ae0\u5c0f\u6d4b\u9a8c",
                "count": 1
            },
            {
                "name": "sp3-1\u90e8\u5206.mp4",
                "count": 1
            },
            {
                "name": "sp3-2.mp4",
                "count": 1
            },
            {
                "name": "sp3-3.mp4",
                "count": 1
            },
            {
                "name": "sp4\uff081-2\u8282\uff09\u90e8\u5206.mp4",
                "count": 1
            },
            {
                "name": "sp4-\u4eff\u771f\u8bb2\u5ea7\uff08\u5b8c\u6574\uff09.mp4",
                "count": 1
            },
            {
                "name": "\u7b2c\u4e09\u7ae0\u7ae0\u8282\u5c0f\u6d4b\u9a8c",
                "count": 1
            },
            {
                "name": "sp5-1\u90e8\u5206.mp4",
                "count": 1
            },
            {
                "name": "SP5-2\u90e8\u5206.mp4",
                "count": 1
            },
            {
                "name": "\u7b2c\u56db\u7ae0\u5c0f\u6d4b\u9a8c",
                "count": 1
            },
            {
                "name": "sp5-3\u90e8\u5206.mp4",
                "count": 1
            },
            {
                "name": "\u7b2c\u4e94\u7ae0\u5c0f\u6d4b\u9a8c",
                "count": 1
            }
        ],
        "learn_curve": {
            "2": 3,
            "3": 13,
            "4": 13
        }

    }

    return render(request, 'TeachingResult.html', message)
