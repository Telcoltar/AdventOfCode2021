from typing import Tuple, List
import logging

# logging.basicConfig(filename="log.log",
#                     filemode="w",
#                     level=logging.INFO,
#                     format="%(asctime)s %(levelname)s %(threadName)s %(name)s: %(message)s",
#                     )

logging.basicConfig(filename="test.log", level=logging.INFO)

logging.info("Hi")


def get_input(filename: str) -> List[Tuple[str, int]]:
    with open(filename) as f:
        data_list = [line.split() for line in f.readlines()]
        data_list = [(p[0], int(p[1])) for p in data_list]
        return data_list


def solution_part_1(input_data: List[Tuple[str, int]]) -> int:
    direction: str = ""
    num: int = 0
    current = [0, 0]
    for direction, num in input_data:
        logging.debug(f"{current}, {direction}, {num}")
        if direction == "forward":
            current[0] += num
        elif direction == "down":
            current[1] += num
        else:
            current[1] -= num
    logging.debug(f"{current}, {direction}, {num}")
    return current[0]*current[1]


def solution_part_2(input_data: List[Tuple[str, int]]) -> int:
    current = [0, 0, 0]
    for direction, num in input_data:
        if direction == "forward":
            current[0] += num
            current[1] += current[2]*num
        elif direction == "down":
            current[2] += num
        else:
            current[2] -= num
    return current[0] * current[1]


if __name__ == "__main__":
    logging.info("="*20 + " Part 1 " + "="*20)
    logging.info(solution_part_1(get_input("../example.txt")))
    logging.info(solution_part_1(get_input("../input.txt")))
    logging.info("="*20 + " Part 2 " + "="*20)
    logging.info(solution_part_2(get_input("../example.txt")))
    logging.info(solution_part_2(get_input("../input.txt")))
