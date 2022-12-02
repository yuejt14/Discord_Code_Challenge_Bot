import json

import requests

from src import common

BASE_URL = 'https://leetcode.com'
API_URL = BASE_URL + '/api/problems/algorithms/'
QUESTION_URL = BASE_URL + '/problems/{question_title_slug}'
SUBMIT_URL = BASE_URL + '/problems/{question_title_slug}/submit/'
SUBMISSION_URL = BASE_URL + '/problems/{question_title_slug}/submissions'
SUBMISSION_CHECK_URL = BASE_URL + '/submissions/detail/{id}/check'
GRAPHQL_URL = BASE_URL + '/graphql'


# cookies = {
#     'csrftoken': os.getenv('CSRF_TOKEN'),
#     'LEETCODE_SESSION': os.getenv('LEETCODE_SESSION'),
# }

def get_info(problem, cookies):
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


def submit(code: str, lang: str, problem, cookies):
    body = {
        'question_id': problem['stat']['question_id'],
        'lang': common.get_lang(lang),
        'typed_code': code
    }
    headers = {
        'origin': BASE_URL,
        'Referer': SUBMISSION_URL.format(question_title_slug=problem['stat']['question__title_slug']),
        'Content-Type': 'application/json',
        'X-CSRFToken': cookies['csrftoken'],
    }
    submit_url = SUBMIT_URL.format(question_title_slug=problem['stat']['question__title_slug'])
    r = retrieve(submit_url, method='POST', data=json.dumps(body),
                 headers=headers, cookies=cookies)
    text = r.text.encode('utf-8')
    print(text)

    data = json.loads(text)

    return data['submission_id']


def check_submission_result(submission_id, cookies):
    print('Checking submission for id:', submission_id)

    url = SUBMISSION_CHECK_URL.format(id=submission_id)
    r = retrieve(url, cookies=cookies)
    if r.status_code != 200:
        return "Request Failed!"
    text = r.text.encode('utf-8')
    data = json.loads(text)
    if data['run_success']:
        return f'Success!\nRuntime: {data["status_runtime"]} memory: {data["memory"]}'
    else:
        return r.text


def retrieve(url, cookies, headers=None, method='GET', data=None, ):
    r = None
    if method == 'GET':
        r = requests.get(url, headers=headers, cookies=cookies)
    elif method == 'POST':
        r = requests.post(url, headers=headers, data=data, cookies=cookies)
    return r
