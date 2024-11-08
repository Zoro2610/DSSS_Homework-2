import unittest
from math_quiz import generate_random_integer, generate_random_operator, generate_math_problem


class TestMathGame(unittest.TestCase):

    def test_generate_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val, f"{rand_num} is not in range [{min_val}, {max_val}]")

    def test_generate_random_operator(self):
        valid_operators = ['+', '-', '*']
        for _ in range(1000):  # Test a large number of random values
             operator = generate_random_operator()
             self.assertIn(operator, valid_operators, f"Operator {operator} is not in the list of valid operators")
        

    def test_generate_math_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (10, 3, '-', '10 - 3', 7),
                (4, 5, '*', '4 * 5', 20),
                (0, 10, '+', '0 + 10', 10),
                (12, 0, '-', '12 - 0', 12),
                (5, 0, '*', '5 * 0', 0),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = generate_math_problem(num1, num2, operator)
                self.assertEqual(problem, expected_problem, f"Expected problem '{expected_problem}', but got '{problem}'")
                self.assertEqual(answer, expected_answer, f"Expected answer '{expected_answer}', but got '{answer}'")
                

if __name__ == "__main__":
    unittest.main()
