from unittest import TestCase
from main import solution_part_1, get_input, solution_part_2


class Test(TestCase):
    def test_solution_part_1(self):
        self.assertEqual(solution_part_1(get_input("../example.txt")), 198)

    def test_solution_part_2(self):
        self.assertEqual(solution_part_2(get_input("../example.txt")), 230)


