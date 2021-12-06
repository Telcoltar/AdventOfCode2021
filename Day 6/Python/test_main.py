from unittest import TestCase
from main import solution, get_input_data


class Test(TestCase):
    def test_solution_part_1(self):
        self.assertEqual(solution(get_input_data("../example.txt"), 80), 5934)

    def test_solution_part_2(self):
        self.assertEqual(solution(get_input_data("../example.txt"), 256), 26984457539)
