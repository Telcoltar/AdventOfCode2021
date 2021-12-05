import logging
from typing import List, Tuple
from Board import Board

logging.basicConfig(filename="log.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(threadName)s %(name)s: %(message)s",
                    level=logging.DEBUG)


def get_input(filename: str) -> Tuple[List[int], List[Board]]:
    with open(filename) as f:
        drawed_numbers = [int(num) for num in f.readline().split(",")]
        f.readline()
        current_row = f.readline().strip()
        boards = []
        size = len(current_row.split())
        while current_row != "":
            current_board = []
            for i in range(size):
                current_board.append([int(num) for num in current_row.split()])
                current_row = f.readline().strip()
            boards.append(Board(current_board))
            current_row = f.readline().strip()
        return drawed_numbers, boards


def solution_part_1(input_data: Tuple[List[int], List[Board]]) -> int:
    drawed_numbers, boards = input_data
    for num in drawed_numbers:
        for b in boards:
            status = b.draw_number(num)
            if status != 0:
                logging.debug(num)
                return status * num


def solution_part_2(input_data: Tuple[List[int], List[Board]]) -> int:
    drawed_numbers, boards = input_data
    del_list = []
    last = 0
    for num in drawed_numbers:
        for i, b in enumerate(boards):
            status = b.draw_number(num)
            if status != 0:
                logging.debug(num)
                logging.debug(status * num)
                last = status * num
                del_list.append(i)
        del_list.reverse()
        for i in del_list:
            boards.pop(i)
        del_list = []
    return last


if __name__ == "__main__":
    logging.debug("=" * 20 + "Part 1" + "=" * 20)
    logging.debug(solution_part_1(get_input("../example.txt")))
    logging.info(solution_part_1(get_input("../input.txt")))
    logging.debug("="*20 + "Part 2" + "="*20)
    logging.debug(solution_part_2(get_input("../example.txt")))
    logging.info(solution_part_2(get_input("../input.txt")))