from unittest import TestCase
from main import solution_part_1, get_input_data


class Test(TestCase):
    def test_solution_part_1(self):
        self.assertEqual(solution_part_1(get_input_data("../example.txt")), 15)
