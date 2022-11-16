import json
import requests

BASE_URL = 'https://leetcode.com'
API_URL = BASE_URL + '/api/problems/algorithms/'
SUBMISSION_URL = BASE_URL + '/submissions/detail/{id}/check'


def submit(code: str):
    from config import cookies
    body = {'question_id': 1,
            'test_mode': False,
            'lang': 'python3',
            'judge_type': 'large',
            'typed_code': code}

    headers = {
        'Referer': 'https://leetcode.com/problems/two-sum',
        'X-CSRFToken': cookies['csrftoken'],
    }

    r = retrieve('https://leetcode.com/problems/two-sum/submit/', method='POST', data=json.dumps(body),
                 headers=headers)
    text = r.text.encode('utf-8')
    data = json.loads(text)
    return data['submission_id']


def check_submission_result(submission_id):
    url = SUBMISSION_URL.format(id=submission_id)
    retrieve(url)


def retrieve(url, headers=None, method='GET', data=None):
    from config import cookies
    r = None
    if method == 'GET':
        r = requests.get(url, headers=headers, cookies=cookies)
    elif method == 'POST':
        r = requests.post(url, headers=headers, data=data, cookies=cookies)
    print(r.text)
    return r


code_example = "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        values   = set(nums).intersection(target-n for n in set(nums)) # matching values\n        v1,v2    = min(values),max(values)           # complementary values\n        i1       = nums.index(v1)                    # indexes of 1st value\n        i2       = nums.index(v2,(i1+1)*(v1==v2))    # index of second value\n        return i1,i2"

# sub_id = submit(code_example)
check_submission_result(844199041)
