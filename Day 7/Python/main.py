import logging
from typing import List, Callable

logging.basicConfig(filename="log.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(threadName)s %(name)s: %(message)s",
                    level=logging.DEBUG)


def get_input_data(filename: str) -> List[int]:
    with open(filename) as f:
        return [int(num) for num in f.readline().strip().split(",")]


def solution_part_1(nums: List[int]):
    return solution(nums, lambda current, num_list: sum([abs(num - current) for num in nums]))


def solution_part_2(nums: List[int]):
    calc_distance: Callable[[int], int] = lambda val: val*(val + 1) // 2
    return solution(nums, lambda current, num_list: sum([calc_distance(abs(num - current)) for num in nums]))


def solution(nums: List[int], get_value: Callable[[int, List[int]], int]) -> int:
    nums.sort()
    mid = len(nums) // 2
    logging.debug(nums[mid])
    current = max(nums)
    last_num = get_value(current, nums)
    step = -current//10
    current += step
    counter = 0
    while abs(step) > 1 and counter < 1000:
        logging.debug(f"Step: {step}, Current: {current}, Last: {last_num},"
                      f"New: {get_value(current, nums)}")
        if last_num > get_value(current, nums):
            last_num = get_value(current, nums)
            current += step
        else:
            last_num = get_value(current, nums)
            step = -step//2
            current += step
        counter += 1
    while get_value(current, nums) < last_num:
        last_num = get_value(current, nums)
        current += step
        logging.debug(f"Step: {step}, Current: {current}, Last: {last_num},"
                      f"New: {get_value(current, nums)}")
    return last_num


if __name__ == "__main__":
    logging.debug(solution_part_1(get_input_data("../example.txt")))
    logging.info(solution_part_1(get_input_data("../input.txt")))
    logging.debug(solution_part_2(get_input_data("../example.txt")))
    logging.info(solution_part_2(get_input_data("../input.txt")))