import logging
from typing import List

logging.basicConfig(filename="log.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(threadName)s %(name)s: %(message)s",
                    level=logging.DEBUG)


def get_input_data(filename: str) -> List[int]:
    with open(filename) as f:
        return list(map(int, f.readline().strip().split(",")))


def solution(input_data: List[int], cycles: int) -> int:
    status = {i: 0 for i in range(9)}
    for state in input_data:
        status[state] += 1
    logging.debug(status)
    for _ in range(cycles):
        new = status[0]
        for i in range(8):
            status[i] = status[i + 1]
        status[8] = new
        status[6] += new
    return sum([status[i] for i in status])


if __name__ == "__main__":
    logging.debug(solution(get_input_data("../example.txt"), 80))
    logging.info(solution(get_input_data("../input.txt"), 80))
    logging.debug(solution(get_input_data("../example.txt"), 256))
    logging.info(solution(get_input_data("../input.txt"), 256))