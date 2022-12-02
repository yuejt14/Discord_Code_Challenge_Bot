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
        client = LeetCodeClient()
        client.refresh_cookies(get_cookies())
        code_text = load_file_text('solutions/two_sum_python_valid.txt')

        a = client.submit(code_text, 'python')
        print(a)

        self.assertTrue('FOO'.isupper())


if __name__ == '__main__':
    unittest.main()
