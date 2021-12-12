from unittest import TestCase
from main import solution_part_1, solution_part_2, get_input_data


class Test(TestCase):
    def test_solution_part_1(self):
        self.assertEqual(solution_part_1(get_input_data("../example.txt")), 37)

    def test_solution_part_2(self):
        self.assertEqual(solution_part_2(get_input_data("../example.txt")), 168)