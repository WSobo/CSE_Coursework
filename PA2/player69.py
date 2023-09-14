import random


class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark


class AI(Player):
    def __init__(self, name, mark):
        super().__init__(name, mark)

    def choose_move(self, board):
        empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
        move = random.choice(empty_cells)
        return move


class MiniMax(AI):
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
