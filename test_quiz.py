import quiz
import unittest
from unittest import TestCase

class TestQuiz(TestCase):

    def test_quiz_with_string_answers(self):
        right_answer = 'Madison'
        user_answer = 'Madison'

        result = quiz.is_correct_answer(right_answer, user_answer)
        self.assertTrue(result)

    def test_quiz_different_cases(self):
        right_answer = 'Madison'
        user_answer = 'MADISON'

        result = quiz.is_correct_answer(right_answer, user_answer)
        self.assertTrue(result)

    def test_quiz_answer_has_spaces(self):
        possible_user_answers = {'Madison': ' Madison', 'Madison': 'Madison ', 'Madison': '  Madison '}
        for right_answer, user_answer in possible_user_answers.items():
            result = quiz.is_correct_answer(right_answer, user_answer)
            self.assertTrue(result)

    def test_quiz_reports_wrong_answer(self):
        right_answer = 'Madison'
        user_answer = 'St. Paul'
        result = quiz.is_correct_answer(right_answer, user_answer)
        self.assertFalse(result)

    def test_quiz_numeric_answers(self):
        right_answer = 42
        user_answer = 42
        result = quiz.is_correct_answer(right_answer, user_answer)
        self.assertTrue(result)

    def test_quiz_numeric_answers_incorrect(self):
        right_answer = 42
        user_answer = 120020
        result = quiz.is_correct_answer(right_answer, user_answer)
        self.assertFalse(result)

    def test_quiz_numeric_and_string(self):
        right_answer = 100
        user_answer = '100'
        result = quiz.is_correct_answer(right_answer, user_answer)
        self.assertTrue(result)



if __name__ == '__main__':
    unittest.main()