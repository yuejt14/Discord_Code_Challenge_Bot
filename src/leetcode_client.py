import json
import time

from src import leetcode_api

PROBLEM_LIST_JSON_FILE = '../problems_list.json'


def load_problem_list():
    with open(PROBLEM_LIST_JSON_FILE, 'r') as problem_list_file:
        problem_list_object = json.load(problem_list_file)
    return problem_list_object['stat_status_pairs']


def parse_submission_result(result):
    print(result)
    result_string = ''
    if result.get('run_success'):
        result_string = f'Success!\nRuntime: {result["status_runtime"]} memory: {result["memory"]}'
    else:
        if result.get('error'):
            result_string += f'Error: {result.get("error")}\n'
        if result.get('runtime_error'):
            result_string += f'runtime_error: {result.get("runtime_error")}\n'
        if result.get('last_testcase'):
            result_string += f'last_testcase: {result.get("last_testcase")}\n'
        if result.get('expected_output'):
            result_string += f'expected_output: {result.get("expected_output")}\n'
    return result_string


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
        if not self.current_problem:
            return {'Current problem is not set, submission failed'}
        if not self.cookies:
            return {'error': 'Leetcode Cookie is not set, submission failed'}

        # return leetcode_api.submit(code, lang, self.current_problem, self.cookies)
        submission = leetcode_api.submit(code, lang, self.current_problem, self.cookies)
        return submission

    def check_result(self, submission_id):
        # check submission result
        result = leetcode_api.check_submission_result(submission_id, self.cookies)
        return result

    def submit_and_check(self, code, lang):
        submission = self.submit(code, lang)

        submission_id = submission.get('submission_id')
        if not submission_id:
            return parse_submission_result(submission)
        time.sleep(5)
        result = self.check_result(submission_id)

        return parse_submission_result(result)
