import json

from src import leetcode_api

PROBLEM_LIST_JSON_FILE = '../problems_list.json'


def load_problem_list():
    with open(PROBLEM_LIST_JSON_FILE, 'r') as problem_list_file:
        problem_list_object = json.load(problem_list_file)
    return problem_list_object['stat_status_pairs']


class LeetCodeClient:
    def __init__(self):
        self.problem_list = load_problem_list()
        self.current_problem = None
        self.update_current_problem(1)
        self.cookies = None

    def refresh_cookies(self, cookies):
        self.cookies = cookies

    def update_current_problem(self, question_id=None):
        if question_id:
            new_question_id = question_id
        else:
            new_question_id = self.current_problem['stat']['question_id'] + 1
        self.current_problem = self.problem_list[-new_question_id]

    def submit(self, code, lang):
        return leetcode_api.submit(code, lang, self.current_problem, self.cookies)
