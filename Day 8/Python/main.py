import logging
from typing import List, Tuple, Dict

logging.basicConfig(filename="log.log",
                    filemode="w",
                    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
                    level=logging.DEBUG)

valid_patterns: List[Tuple[int, ...]] = [
    (1, 1, 1, 0, 1, 1, 1),  # 0
    (0, 0, 1, 0, 0, 1, 0),  # 1
    (1, 0, 1, 1, 1, 0, 1),  # 2
    (1, 0, 1, 1, 0, 1, 1),  # 3
    (0, 1, 1, 1, 0, 1, 0),  # 4
    (1, 1, 0, 1, 0, 1, 1),  # 5
    (1, 1, 0, 1, 1, 1, 1),  # 6
    (1, 0, 1, 0, 0, 1, 0),  # 7
    (1, 1, 1, 1, 1, 1, 1),  # 8
    (1, 1, 1, 1, 0, 1, 1)  # 9
]


def check_unique_digits(number: int) -> bool:
    return number == 2 or number == 3 or number == 4 or number == 7


def check_len_of_pattern(p: str) -> bool:
    p_len = len(p)
    return p_len != 2 and p_len != 3 and p_len != 4 and p_len != 7


def get_special_patterns(patterns: List[str]) -> (str, str, str):
    ret = ["", "", ""]
    for p in patterns:
        if len(p) == 2:
            ret[0] = p
        elif len(p) == 3:
            ret[1] = p
        elif len(p) == 4:
            ret[2] = p
    return ret


def get_input_data(filename: str) -> List[Tuple[List[str], ...]]:
    with open(filename) as f:
        return [tuple(map(str.split, line.split("|"))) for line in f.readlines()]


def parse_pattern(pattern: str, position: Dict[str, int]) -> tuple[int, ...]:
    parsed_pattern = [0 for _ in range(7)]
    for mark in pattern:
        parsed_pattern[position[mark]] = 1
    return tuple(parsed_pattern)


def build_possible_positions(one, seven, four):
    rem_sev = "a"
    for mark in seven:
        if mark not in one:
            rem_sev = mark
            break
    rem_four = []
    for mark in four:
        if mark not in one:
            rem_four.append(mark)
    rem_marks = []
    used_marks = four + rem_sev
    for mark in "abcdefg":
        if mark not in used_marks:
            rem_marks.append(mark)
    possible_positions = [[rem_sev] + ["a"] * 6 for _ in range(8)]
    for i in range(4):
        possible_positions[i][1] = rem_four[0]
        possible_positions[i][3] = rem_four[1]
        possible_positions[i + 4][1] = rem_four[1]
        possible_positions[i + 4][3] = rem_four[0]
    for i in range(2):
        possible_positions[i][2] = one[0]
        possible_positions[i][5] = one[1]
        possible_positions[i + 2][2] = one[1]
        possible_positions[i + 2][5] = one[0]
        possible_positions[i + 4][2] = one[0]
        possible_positions[i + 4][5] = one[1]
        possible_positions[i + 6][2] = one[1]
        possible_positions[i + 6][5] = one[0]
    for i in range(0, 8, 2):
        possible_positions[i][4] = rem_marks[0]
        possible_positions[i][6] = rem_marks[1]
    for i in range(1, 8, 2):
        possible_positions[i][4] = rem_marks[1]
        possible_positions[i][6] = rem_marks[0]
    return ["".join(pos) for pos in possible_positions]
    

def solution_part_1(input_data: List[Tuple[List[str], ...]]):
    numbers = [datum[1] for datum in input_data]
    num_len = [list(map(len, datum)) for datum in numbers]
    num_filtered = [len(list(filter(check_unique_digits, datum))) for datum in num_len]
    total_nums = sum(num_filtered)
    logging.debug(num_filtered)
    return total_nums


def solution_part_2(input_data: List[Tuple[List[str], ...]]):
    parsed_data = []
    for patterns, digits in input_data:
        possible_positions = build_possible_positions(*get_special_patterns(patterns))
        possible_positions_parsed: List[Dict[str, int]] = [{mark: i for i, mark in enumerate(positions)} for positions in possible_positions]
        patterns = list(filter(check_len_of_pattern, patterns))
        logging.debug("=" * 30)
        logging.debug(f"Patterns: {patterns}, Digits: {digits}")
        current_pos_positions: List[int] = list(range(8))
        new_pos_positions: List[int] = []
        correct_pos: Dict[str, int] = {}
        parsed_digits: List[str] = []
        for pattern in patterns:
            logging.debug(f"Pattern: {pattern}, Current possible positions: {current_pos_positions}")
            for pos in current_pos_positions:
                parsed_pattern = parse_pattern(pattern, possible_positions_parsed[pos])
                logging.debug(parsed_pattern)
                if parsed_pattern in valid_patterns:
                    new_pos_positions.append(pos)
            if len(new_pos_positions) == 1:
                logging.debug(new_pos_positions)
                correct_pos = possible_positions_parsed[new_pos_positions[0]]
                break
            else:
                current_pos_positions = new_pos_positions
                new_pos_positions = []
        for d in digits:
            d_parsed = parse_pattern(d, correct_pos)
            parsed_digits.append(str(valid_patterns.index(d_parsed)))
        logging.debug(parsed_digits)
        parsed_data.append(int("".join(parsed_digits)))
    logging.debug(parsed_data)
    return sum(parsed_data)


if __name__ == "__main__":
    logging.debug(solution_part_1(get_input_data("../example.txt")))
    logging.info(solution_part_1(get_input_data("../input.txt")))
    logging.debug(solution_part_2(get_input_data("../example.txt")))
    logging.info(solution_part_2(get_input_data("../input.txt")))
