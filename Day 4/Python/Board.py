from typing import List


class Board:

    def __init__(self, board: List[List[int]]):
        self.board = board
        self.num_2_coords = {}
        self.size = len(self.board)
        for i, row in enumerate(board):
            for j, value in enumerate(row):
                self.num_2_coords[value] = (i, j)
        self.columns = [0] * self.size
        self.rows = [0] * self.size

    def draw_number(self, num: int) -> int:
        if num in self.num_2_coords:
            (row, col) = self.num_2_coords[num]
            self.board[row][col] = 0
            self.columns[col] += 1
            if self.columns[col] == self.size:
                return self.sum_remaining()
            self.rows[row] += 1
            if self.rows[row] == self.size:
                return self.sum_remaining()
        return 0

    def sum_remaining(self) -> int:
        sum_rem = 0
        for row in self.board:
            for val in row:
                sum_rem += val
        return sum_rem
