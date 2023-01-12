import os
import unittest

from dotenv import load_dotenv

from src.leetcode_client import LeetCodeClient

load_dotenv()
TWO_SUM_PYTHON_SOLUTION = ""


def load_file_text(file_name: str):
    with open(file_name, 'r') as f:
        f_text = f.read()
    return f_text


def get_cookies():
    cookies = {
        'csrftoken': os.getenv('CSRF_TOKEN'),
        'LEETCODE_SESSION': os.getenv('LEETCODE_SESSION'),
    }
    return cookies


class TestClient(unittest.TestCase):

    def test_submission(self):
        # submit
        client = LeetCodeClient()
        client.refresh_cookies(get_cookies())
        code_text = load_file_text('solutions/two_sum_python_valid.txt')
        submission_result = client.submit(code_text, 'python')
        self.assertTrue(submission_result.get('submission_id'))

    def test_submission_failed_miss_cookie(self):
        client = LeetCodeClient()
        code_text = load_file_text('solutions/two_sum_python_valid.txt')
        submission_result = client.submit(code_text, 'python')
        self.assertFalse(submission_result.get('submission_id'))
        self.assertTrue(submission_result.get('error') == 'Leetcode Cookie is not set, submission failed')

    def test_submission_invalid_cookies(self):
        client = LeetCodeClient()
        invalid_cookies = {
            'csrftoken': "CNlAVWyV5YOyr5v7i8YeXJJi80JdJf90nclky5Z7EZ3H8yDVMK8fdObhceUPJn2a",
            'LEETCODE_SESSION': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNTA4NzAyMyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiNTViYjI5ODdlNmFkYzBhZTI3NmE2N2ExMjA1ZDVkNzRhOGExNDcwZiIsImlkIjo1MDg3MDIzLCJlbWFpbCI6Inl1ZXRob21wc29uQGdtYWlsLmNvbSIsInVzZXJuYW1lIjoieXVlanQxNCIsInVzZXJfc2x1ZyI6Inl1ZWp0MTQiLCJhdmF0YXIiOiJodHRwczovL3MzLXVzLXdlc3QtMS5hbWF6b25hd3MuY29tL3MzLWxjLXVwbG9hZC9hc3NldHMvZGVmYXVsdF9hdmF0YXIuanBnIiwicmVmcmVzaGVkX2F0IjoxNjczNTU5NzQ5LCJpcCI6IjczLjI1MC4xNzMuMTk2IiwiaWRlbnRpdHkiOiJhODE4YWIzNTk4MDQ1MTdmMjU0OWU5NGM4OGQwM2MwYiIsInNlc3Npb25faWQiOjMzNjA0NTg0LCJfc2Vzc2lvbl9leHBpcnkiOjEyMDk2MDB9.wTK1vwU3L2gP2LYBzc6v0w-ikPfdeE9tsqXYrY5Tc0a'
        }
        client.refresh_cookies(invalid_cookies)
        code_text = load_file_text('solutions/two_sum_python_valid.txt')
        submission_result = client.submit(code_text, 'python')
        self.assertTrue(submission_result == {'error': 'User is not authenticated'})

    def test_submit_and_check(self):
        # submit
        client = LeetCodeClient()
        client.refresh_cookies(get_cookies())
        code_text = load_file_text('solutions/two_sum_python_valid.txt')
        result = client.submit_and_check(code_text, 'python')

        print(result)
        self.assertTrue('s')

    def test_submit_and_check_failed(self):
        # submit
        client = LeetCodeClient()
        client.refresh_cookies(get_cookies())
        code_text = load_file_text('solutions/two_sum_python_invalid.txt')
        result = client.submit_and_check(code_text, 'python')
        print(result)
        self.assertTrue('s')


if __name__ == '__main__':
    unittest.main()
