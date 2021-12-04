from unittest import TestCase
from main import solution_part_1, solution_part_2, get_input


class Test(TestCase):
    def test_solution_part_1(self):
        self.assertEqual(solution_part_1(get_input("../example.txt")), 150)

    def test_solution_part_2(self):
        self.assertEqual(solution_part_2(get_input("../example.txt")), 900)