import json
import time

import requests

BASE_URL = 'https://leetcode.com'
API_URL = BASE_URL + '/api/problems/algorithms/'
SUBMIT_URL = BASE_URL + '/problems/{question_title_slug}/submit/'
SUBMISSION_URL = BASE_URL + '/problems/{question_title_slug}/submissions'
SUBMISSION_CHECK_URL = BASE_URL + '/submissions/detail/{id}/check'

problem = {
    "stat": {
        "question_id": 1,
        "question__article__live": True,
        "question__article__slug": "two-sum",
        "question__article__has_video_solution": True,
        "question__title": "Two Sum",
        "question__title_slug": "two-sum",
        "question__hide": True,
        "total_acs": 8283892,
        "total_submitted": 16878262,
        "frontend_question_id": 1,
        "is_new_question": True
    },
    "status": "ac",
    "difficulty": {
        "level": 1
    },
    "paid_only": False,
    "is_favor": False,
    "frequency": 0,
    "progress": 0
}


def submit(code: str):
    from config import cookies
    body = {'question_id': problem['stat']['question_id'],
            'lang': 'python3',
            'typed_code': code}

    headers = {
        'origin': BASE_URL,
        'Referer': SUBMISSION_URL.format(question_title_slug=problem['stat']['question__title_slug']),
        'Content-Type': 'application/json',

        'X-CSRFToken': cookies['csrftoken'],
    }
    submit_url = SUBMIT_URL.format(question_title_slug=problem['stat']['question__title_slug'])
    r = retrieve(submit_url, method='POST', data=json.dumps(body),
                 headers=headers)
    text = r.text.encode('utf-8')
    data = json.loads(text)
    return data['submission_id']


def check_submission_result(submission_id):
    print('Checking submission for id:', submission_id)

    url = SUBMISSION_CHECK_URL.format(id=submission_id)
    r = retrieve(url)
    return r.text


def retrieve(url, headers=None, method='GET', data=None):
    from config import cookies
    r = None
    if method == 'GET':
        r = requests.get(url, headers=headers, cookies=cookies)
    elif method == 'POST':
        r = requests.post(url, headers=headers, data=data, cookies=cookies)
    return r


print(SUBMISSION_URL.format(question_title_slug=problem['stat']['question__title_slug']))
# code_example = "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        values   = set(nums).intersection(target-n for n in set(nums)) # matching values\n        v1,v2    = min(values),max(values)           # complementary values\n        i1       = nums.index(v1)                    # indexes of 1st value\n        i2       = nums.index(v2,(i1+1)*(v1==v2))    # index of second value\n        return i1,i2"
#
# sub_id = submit(code_example)
# time.sleep(5)
#
# r = check_submission_result(sub_id)
# print(r)
