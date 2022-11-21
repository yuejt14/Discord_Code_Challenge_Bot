import common
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = 'https://leetcode.com'
API_URL = BASE_URL + '/api/problems/algorithms/'
QUESTION_URL = BASE_URL + '/problems/{question_title_slug}'
SUBMIT_URL = BASE_URL + '/problems/{question_title_slug}/submit/'
SUBMISSION_URL = BASE_URL + '/problems/{question_title_slug}/submissions'
SUBMISSION_CHECK_URL = BASE_URL + '/submissions/detail/{id}/check'
GRAPHQL_URL = BASE_URL + '/graphql'

problem = {
    "stat": {
        "question_id": 3,
        "question__article__live": True,
        "question__article__slug": "longest-substring-without-repeating-characters",
        "question__article__has_video_solution": True,
        "question__title": "Longest Substring Without Repeating Characters",
        "question__title_slug": "longest-substring-without-repeating-characters",
        "question__hide": False,
        "total_acs": 4027268,
        "total_submitted": 11916587,
        "frontend_question_id": 3,
        "is_new_question": False
    },
    "status": "ac",
    "difficulty": {
        "level": 2
    },
    "paid_only": False,
    "is_favor": False,
    "frequency": 0,
    "progress": 0
}

cookies = {
    'csrftoken': os.getenv('CSRF_TOKEN'),
    'LEETCODE_SESSION': os.getenv('LEETCODE_SESSION'),
}


def get_info():
    query = """query questionData($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            title
            titleSlug
            questionId
            questionFrontendId
            content
            difficulty
            stats
            companyTagStats
            topicTags {
                name
                slug
                __typename
            }
            similarQuestions
            codeSnippets {
                lang
                langSlug
                code
                __typename
            }
            solution {
                id
                canSeeDetail
                __typename
            }
            sampleTestCase
            enableTestMode
            metaData
            enableRunCode
            judgerAvailable
            __typename
        }
    }"""
    headers = {
        'origin': BASE_URL,
        'Referer': QUESTION_URL.format(question_title_slug=problem['stat']['question__title_slug']),
        'Content-Type': 'application/json',
        'X-CSRFToken': cookies['csrftoken'],
    }
    body = {
        "query": query,
        "variables": {"titleSlug": problem['stat']['question__title_slug']},
        "operationName": "questionData"
    }

    r = retrieve(GRAPHQL_URL, headers, method='POST', data=json.dumps(body))
    obj = json.loads(r.text)

    print(r.text)


def submit(code: str, lang: str):
    body = {'question_id': problem['stat']['question_id'],
            'lang': common.get_lang(lang),
            'typed_code': code}
    print(cookies)
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
    if r.status_code != 200:
        return "Request Failed!"
    text = r.text.encode('utf-8')
    data = json.loads(text)
    if data['run_success']:
        return f'Success!\nRuntime: {data["status_runtime"]} memory: {data["memory"]}'
    else:
        return r.text


def retrieve(url, headers=None, method='GET', data=None):
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

get_info()
