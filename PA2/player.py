# author: William Sobolewski
# date: July 13th, 2023
# file: player.py to be used with tictac.py

import random


class Player:
    def __init__(self, name, sign):
        self.name = name
        self.sign = sign

    def get_sign(self):
        return self.sign

    def get_name(self):
        return self.name

    def choose(self, board):
        while True:
            cell = input(
                f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: \n")
            if self.is_valid_cell(cell) and board.isempty(cell):
                board.set(cell, self.sign)
                break
            else:
                print("You did not choose correctly.")

    def is_valid_cell(self, cell):
        return len(cell) == 2 and cell[0].upper() in ['A', 'B', 'C'] and cell[1] in ['1', '2', '3']


class AI(Player):
    def __init__(self, name, mark):
        super().__init__(name, mark)

    def __str__(self):
        return self.name

    def choose_move(self, board):
        empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
        move = random.choice(empty_cells)
        return move


class MiniMax(AI):
    '''
    Minimax:
    1. Check the base case: if the game is over, then return -1 if self lost, 0 if it is a tie, or 1 if self won.
    2. Set the min score to infinity and max score to -infinity
    3. Choose a cell (or make a move): 
            a. iterate through all available cells (9 cells)
            b. check if the cell is empty
            c. mark the cell with X or O (if self then mark it with its sign, otherwise mark it with another sign)
            d. get score by calling the minimax recursively (you need to alternate between self and opponent)
            e. update score: if self then use the max score (compare it to the max score), otherwise use the min score (compare it to the min score)
            f. update move: update the cell index
            g. unmark the cell (make it a space again " ") and reset all other variables that were affected by the game play
    4. If it is the start level (the last level to be executed completely and the last score to be returned) return the move. 
    '''

    def __init__(self, name, mark):
        super().__init__(name, mark)

    def __str__(self):
        return self.name

    def get_available_moves(self, board):
        return [i for i, cell in enumerate(board) if cell == ' ']

    def choose_move(self, board):
        best_score = float('-inf')
        best_move = None

        for move in self.get_available_moves(board):
            board[move] = self.mark
            score = self.minimax(board, False)
            board[move] = ' '

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, board, is_maximizing):
        scores = {'X': 1, 'O': -1, 'tie': 0}

        winner = self.check_winner(board)
        if winner != ' ':
            return scores[winner]

        if self.check_tie(board):
            return scores['tie']

        best_score = float('-inf') if is_maximizing else float('inf')
        for move in self.get_available_moves(board):
            board[move] = self.mark if is_maximizing else self.get_opponent_mark()
            score = self.minimax(board, not is_maximizing)
            board[move] = ' '
            best_score = max(score, best_score) if is_maximizing else min(
                score, best_score)

        return best_score

    def check_winner(self, board):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combination in winning_combinations:
            if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
                return board[combination[0]]

        return ' '

    def check_tie(self, board):
        if ' ' not in board:
            return True
        return False

    def get_opponent_mark(self):
        return 'X' if self.mark == 'O' else 'O'
