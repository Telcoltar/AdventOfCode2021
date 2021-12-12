import logging
from collections import deque
from typing import List, Tuple, Set

logging.basicConfig(filename="log.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
                    level=logging.DEBUG)


def get_input_data(filename: str) -> List[List[int]]:
    grid: List[List[int]] = [[0]]
    with open(filename) as f:
        for line in f.readlines():
            grid.append([9] + [int(height) for height in line.strip()] + [9])
    size = len(grid[1])
    grid[0] = [9] * size
    grid.append([9] * size)
    return grid


def pprint_grid(grid: List[List[int]]) -> str:
    return "\n\t".join(["Grid: "] + ["".join([str(height) for height in row]) for row in grid])


def solution_part_1(grid: List[List[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])
    logging.debug(f"NUmber of rows: {rows}, number of columns: {cols}")
    low_points = []
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            logging.debug(f"Row: {row}, column: {col}")
            val = grid[row][col]
            if (val < grid[row - 1][col] and
                    val < grid[row + 1][col] and
                    val < grid[row][col - 1] and
                    val < grid[row][col + 1]):
                low_points.append(val)
                logging.debug(f"Found low point: {val}")
    logging.debug(low_points)
    return sum([height + 1 for height in low_points])


def solution_part_2(grid: List[List[int]]) -> int:
    visited_points: Set[Tuple[int, int]] = set()
    rows = len(grid)
    cols = len(grid[0])
    sizes = []
    for row in range(1, rows - 1):
        for col in range(1, cols - 1):
            if (row, col) in visited_points:
                continue
            val = grid[row][col]
            if val != 9:
                size = 0
                q = deque()
                q.append((row, col))
                current: Tuple[int, int]
                while len(q) > 0:
                    current = q.popleft()
                    if current in visited_points:
                        continue
                    size += 1
                    logging.debug(current)
                    visited_points.add(current)
                    for i in range(-1, 2, 2):
                        if grid[current[0] + i][current[1]] != 9:
                            q.append((current[0] + i, current[1]))
                        if grid[current[0]][current[1] + i] != 9:
                            q.append((current[0], current[1] + i))
                logging.debug(f"Size: {size}, Start: {row}, {col}")
                sizes.append(size)
    sizes.sort()
    return sizes[-1] * sizes[-2] * sizes[-3]


if __name__ == "__main__":
    # logging.debug(solution_part_1(get_input_data("../example.txt")))
    # logging.info(solution_part_1(get_input_data("../input.txt")))
    logging.debug(solution_part_2(get_input_data("../example.txt")))
    logging.info(solution_part_2(get_input_data("../input.txt")))
