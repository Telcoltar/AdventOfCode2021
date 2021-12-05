import logging
from typing import List, Tuple
from Point import Point

logging.basicConfig(filename="log.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(threadName)s %(name)s: %(message)s",
                    level=logging.DEBUG)


def get_input_data(filename: str) -> Tuple[int, List[Tuple[Point, Point]]]:
    lines = []
    max_val = 0
    with open(filename) as f:
        for line in map(str.strip, f.readlines()):
            line_split = line.split()
            p1, p2 = line_split[0], line_split[2]
            n1, n2 = map(int, p1.split(","))
            max_val = max(max_val, n1, n2)
            p1 = Point(n1, n2)
            n1, n2 = map(int, p2.split(","))
            max_val = max(max_val, n1, n2)
            p2 = Point(n1, n2)
            lines.append((p1, p2))
    return max_val + 1, lines


def get_range_data(p1: Point, p2: Point) -> Tuple[int, int, int]:
    size = 0
    if p1.x < p2.x:
        x_step = 1
        size = p2.x - p1.x
    elif p1.x == p2.x:
        x_step = 0
    else:
        x_step = -1
        size = p1.x - p2.x

    if p1.y < p2.y:
        y_step = 1
        size = p2.y - p1.y
    elif p1.y == p2.y:
        y_step = 0
    else:
        y_step = -1
        size = p1.y - p2.y

    return x_step, y_step, size + 1


def solution(input_data: Tuple[int, List[Tuple[Point, Point]]], is_part_1: bool):
    size, lines = input_data
    logging.debug(size)
    grid = [[0 for _ in range(size)] for _ in range(size)]
    for p1, p2 in lines:
        x_step, y_step, size = get_range_data(p1, p2)
        logging.debug(f"{p1}, {p2}, {x_step}, {y_step}, {size}")
        if x_step != 0 and y_step != 0 and is_part_1:
            continue
        for i in range(size):
            grid[p1.y + i * y_step][p1.x + i * x_step] += 1
    counter = 0
    for row in grid:
        for point in row:
            if point > 1:
                counter += 1
    return counter


if __name__ == "__main__":
    logging.debug(solution(get_input_data("../example.txt"), True))
    logging.info(solution(get_input_data("../input.txt"), True))
    logging.debug(solution(get_input_data("../example.txt"), False))
    logging.info(solution(get_input_data("../input.txt"), False))