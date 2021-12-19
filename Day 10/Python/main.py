import logging
from typing import List
from collections import deque

logging.basicConfig(filename="log.log",
filemode="w",
format="%(asctime)s %(levelname)s %(name)s: %(message)s",
level=logging.DEBUG)

bracket_values_part_1 = {")": 3, "]": 57, "}": 1197, ">": 25137}
bracket_values_part_2 = {")": 1, "]": 2, "}": 3, ">": 4}


def get_input_data(filename: str) -> List[str]:
    with open(filename) as f:
        return list(map(str.strip, f.readlines()))


def get_opposite_bracket(bracket: str) -> str:
    if bracket == "(":
        return ")"
    if bracket == "{":
        return "}"
    if bracket == "[":
        return "]"
    if bracket == "<":
        return ">"
    return bracket


def solution(input_data: List[str]):
    illegal_brackets = []
    incomplete_line_scores = []
    for line in input_data:
        logging.debug(f"Current line {line}")
        illegal = False
        bracket_stack = deque()
        for symb in line:
            if symb in ["(", "[", "{", "<"]:
                bracket_stack.append(symb)
            else:
                expected_bracket = get_opposite_bracket(bracket_stack.pop())
                if symb != expected_bracket:
                    logging.debug(f"Found illegal bracket: {symb}, expected: {expected_bracket}")
                    illegal_brackets.append(symb)
                    illegal = True
                    break
        if not illegal:
            if len(bracket_stack) != 0:
                rem_brackets = list(map(get_opposite_bracket, bracket_stack))
                rem_brackets.reverse()
                logging.debug(rem_brackets)
                score = 0
                for bracket in rem_brackets:
                    score *= 5
                    score += bracket_values_part_2[bracket]
                incomplete_line_scores.append(score)
    logging.debug(f"Illegal brackets: {illegal_brackets}")
    points = 0
    for illegal_bracket in illegal_brackets:
        points += bracket_values_part_1[illegal_bracket]
    incomplete_line_scores.sort()
    mid = (len(incomplete_line_scores) - 1) // 2
    return f"Points part 1: {points}, part 2: {incomplete_line_scores[mid]}"


if __name__ == "__main__":
    logging.debug(solution(get_input_data("../example.txt")))
    logging.info(solution(get_input_data("../input.txt")))