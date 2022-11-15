import json
import browser_cookie3
import http.cookiejar
import requests

# cookies = 'NEW_PROBLEMLIST_PAGE=1; gr_user_id=b314ce77-c206-4f86-b3ef-b55d752fb87b; 87b5a3c3f1a55520_gr_last_sent_cs1=yuejt14; __atuvc=8|45; __stripe_mid=26e80fa1-36eb-4234-a1c6-4572aaa23c702d0c5b; _gid=GA1.2.958684539.1668463038; 87b5a3c3f1a55520_gr_session_id=3d3e3598-2b59-4e12-b6e2-a8928244729c; 87b5a3c3f1a55520_gr_last_sent_sid_with_cs1=3d3e3598-2b59-4e12-b6e2-a8928244729c; 87b5a3c3f1a55520_gr_session_id_3d3e3598-2b59-4e12-b6e2-a8928244729c=true; csrftoken=iF7UWRRG5YqGcP1amYcvIvhdxFayCOrA23IRHidFKBXibcuRWi0gvP87tkRQ9OmF; messages="fb984899d41c351ff65efe917f67437b6b3bea9f$[[\"__json_message\"\0540\05425\054\"Successfully signed in as yuejt14.\"]\054[\"__json_message\"\0540\05425\054\"Successfully signed in as yuejt14.\"]]"; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNTA4NzAyMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTViYjI5ODdlNmFkYzBhZTI3NmE2N2ExMjA1ZDVkNzRhOGExNDcwZiIsImlkIjo1MDg3MDIzLCJlbWFpbCI6Inl1ZXRob21wc29uQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoieXVlanQxNCIsInVzZXJfc2x1ZyI6Inl1ZWp0MTQiLCJhdmF0YXIiOiJodHRwczovL3MzLXVzLXdlc3QtMS5hbWF6b25hd3MuY29tL3MzLWxjLXVwbG9hZC9hc3NldHMvZGVmYXVsdF9hdmF0YXIuanBnIiwicmVmcmVzaGVkX2F0IjoxNjY4NDY2OTQ0LCJpcCI6IjY4LjMzLjM5LjU0IiwiaWRlbnRpdHkiOiI3OTJkZTUxZTRkNWJlNTJhMzVmNTVmMzU3MDE5M2ZjMyIsIl9zZXNzaW9uX2V4cGlyeSI6MTIwOTYwMCwic2Vzc2lvbl9pZCI6MzA4OTM1MDl9.AAttxYDw54rQzRd4_FZsq5tRdKXG8nxAoebNEx4Jmiw; c_a_u="eXVlanQxNA==:1ouiWw:KdCaew07XwCRd7D8wP2IPlGZSbQ"; _gat=1; 87b5a3c3f1a55520_gr_cs1=yuejt14; _ga_CDRWKZTDEX=GS1.1.1668466966.8.1.1668467476.0.0.0; _ga=GA1.1.1298521957.1668058641'

BASE_URL = 'httaaacSom'
cj = http.cookiejar.CookieJar()
cookies = browser_cookie3.chrome()


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6',
    'Host': 'leetcode.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Mobile Safari/537.36',
    'Referer': 'https://leetcode.com/',
}


def submit(code):
    body = {'question_id': 1,
            'test_mode': False,
            'lang': 'python3',
            'judge_type': 'large',
            'typed_code': code}

    csrftoken = 'iF7UWRRG5YqGcP1amYcvIvhdxFayCOrA23IRHidFKBXibcuRWi0gvP87tkRQ9OmF'
    extra_headers = {'Origin': BASE_URL,
                     'Referer': 'https://leetcode.com/problems/two-sum' + '/?tab=Description',
                     'DNT': '1',
                     'Content-Type': 'application/json;charset=UTF-8',
                     'Accept': 'application/json',
                     'X-CSRFToken': csrftoken,
                     'X-Requested-With': 'XMLHttpRequest'}

    newheaders = merge_two_dicts(headers, extra_headers)

    r = retrieve('https://leetcode.com/problems/two-sum/submit/', method='POST', data=json.dumps(body),
                 headers=newheaders)
    if r.status_code != 200:
        return (False, 'Request failed!')
    text = r.text.encode('utf-8')
    try:
        data = json.loads(text)
    except Exception:
        return (False, text)

    if 'error' in data:
        return (False, data['error'])
    return (True, data['submission_id'])


def retrieve(url, headers=None, method='GET', data=None):
    r = None
    if method == 'GET':
        r = requests.get(url, headers=headers, cookies=cookies)
    elif method == 'POST':
        r = requests.post(url, headers=headers, data=data, cookies=cookies)
    print(r.text)
    return r



def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    z = x.copy()
    z.update(y)
    return z


# client = requests.session()
# print(type(client.cookies))

code = "class Solution:\n    def twoSum(self, nums: List[int], target: int) -> List[int]:\n        values   = set(nums).intersection(target-n for n in set(nums)) # matching values\n        v1,v2    = min(values),max(values)           # complementary values\n        i1       = nums.index(v1)                    # indexes of 1st value\n        i2       = nums.index(v2,(i1+1)*(v1==v2))    # index of second value\n        return i1,i2"

submit(code)
