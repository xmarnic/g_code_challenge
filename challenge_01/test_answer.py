import unittest
from shunting import answer

class TestAnswerFunction(unittest.TestCase):

    def setUp(self):
        pass
        self.testCases = ['2+3*2', '2*4*3+9*3+5']
        self.expected = ['232*+', '243**93*5++']

    def test_answer_with_given_test_cases(self):
        for i, test in enumerate(self.testCases):
            reversePolish = answer(test)
        self.assertEqual(reversePolish, self.expected[i])


if __name__ == '__main__':
    unittest.main()
