# author: William Sobolewski
# date: July 13th, 2023
# file: board.py to be used with tictac.py


from player import Player, AI, MiniMax


class Board:
    def __init__(self):
        self.sign = " "
        self.size = 3
        self.board = list(self.sign * self.size ** 2)
        self.winner = ""

    def get_size(self):
        return self.size

    def get_winner(self):
        return self.winner

    def set(self, cell, sign):
        index = self.convert_cell_to_index(cell)
        if self.isempty(cell):
            self.board[index] = sign

    def isempty(self, cell):
        index = self.convert_cell_to_index(cell)
        return self.board[index] == self.sign

    def isdone(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != self.sign:
                self.winner = self.board[combination[0]]
                return True

        if self.sign not in self.board:
            self.winner = "tie"
            return True

        return False

    def show(self):
        print(f"\n   A   B   C ")
        print(f" +---+---+---+")
        print(f"1| {self.board[0]} | {self.board[1]} | {self.board[2]} |")
        print(f" +---+---+---+")
        print(f"2| {self.board[3]} | {self.board[4]} | {self.board[5]} |")
        print(f" +---+---+---+")
        print(f"3| {self.board[6]} | {self.board[7]} | {self.board[8]} |")
        print(f" +---+---+---+")

    def convert_cell_to_index(self, cell):
        column = cell[0].upper()
        row = int(cell[1])
        column_index = ord(column) - ord('A')
        row_index = row - 1
        return row_index * self.size + column_index
