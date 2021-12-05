import logging
from typing import List, Callable

logging.basicConfig(filename="log.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(threadName)s %(name)s: %(message)s",
                    level=logging.DEBUG)


def get_input(filename: str) -> List[str]:
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


def solution_part_1(input_data: List[str]) -> int:
    output_g = ""
    output_e = ""
    logging.debug(len(input_data))
    mid = len(input_data) / 2
    for j in range(len(input_data[0])):
        current = 0
        for i in range(len(input_data)):
            current += int(input_data[i][j])
        if current > mid:
            output_g += "1"
            output_e += "0"
        else:
            output_g += "0"
            output_e += "1"
    logging.debug(output_g)
    logging.debug(output_e)
    gamma = int(output_g, 2)
    logging.debug(gamma)
    epsilon = int(output_e, 2)
    logging.debug(epsilon)
    return gamma * epsilon


def count_ones(input_data: List[str], bit_position: int) -> int:
    count = 0
    for num in input_data:
        count += int(num[bit_position])
    return count


def construct_new_data(input_data: List[str], bit_position: int, mark: str) -> List[str]:
    output_data = []
    for value in input_data:
        if value[bit_position] == mark:
            output_data.append(value)
    return output_data


def trim_down_data(input_data: List[str], mark_function: Callable[[int, int], str]) -> int:
    bit_position = 0
    while len(input_data) > 1:
        ones = count_ones(input_data, bit_position)
        logging.debug(f"Ones: {ones}")
        zeros = len(input_data) - ones
        mark = mark_function(zeros, ones)
        logging.debug(f"Mark: {mark}")
        input_data = construct_new_data(input_data, bit_position, mark)
        bit_position += 1
    return int(input_data[0], 2)


def solution_part_2(input_data: List[str]) -> int:
    # find oxygen rating
    # copy_input_data
    oxygen = trim_down_data(input_data, lambda zeros, ones: "0" if zeros > ones else "1")
    logging.debug(f"Oxygen: {oxygen}")
    co2 = trim_down_data(input_data, lambda zeros, ones: "1" if zeros > ones else "0")
    logging.debug(f"Oxygen: {co2}")
    return oxygen * co2


if __name__ == "__main__":
    logging.debug(f"Example Part 1: {solution_part_1(get_input('../example.txt'))}")
    logging.info(f"Solution Part 1: {solution_part_1(get_input('../input.txt'))}")
    logging.debug(f"Example Part 2: {solution_part_2(get_input('../example.txt'))}")
    logging.info(f"Solution Part 2: {solution_part_2(get_input('../input.txt'))}")
