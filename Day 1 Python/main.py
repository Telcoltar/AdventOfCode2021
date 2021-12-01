from typing import List
import logging


logging.basicConfig(filename="output.txt", filemode="w", level=logging.INFO)


def get_input(filename: str) -> List[int]:
    with open(filename) as f:
        return [int(number_str) for number_str in f.readlines()]


def solution_part_1(input_data: List[int]) -> int:
    current_num: int = input_data[0]
    nums_of_increase: int = 0
    for num in input_data[1:]:
        if current_num < num:
            nums_of_increase += 1
        current_num = num
    return nums_of_increase


def solution_part_2(input_data: List[int]) -> int:
    parsed_data = []
    for i in range(len(input_data) - 2):
        parsed_data.append(sum(input_data[i:i+3]))
    return solution_part_1(parsed_data)


if __name__ == "__main__":
    logging.info(f"Solution Part 1 {solution_part_1(get_input('input1.txt'))}")
    logging.info(f"Solution Part 2 {solution_part_2(get_input('input1.txt'))}")
