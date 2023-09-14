class TicTacToe:
    def __init__(self, marks: list, user1="Bob", user2="Alice"):
        self.marks = [' '] * 9
        self.XorO = ('X', 'O')
        self.players = [user1, user2]
        self.current_player = 0
        self.winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

    def TTT_game(self):
        print("Welcome to TIC-TAC-TOE Game!\n")

        while True:
            self.play_game()

            play_again = input("Would you like to play again? [Y/N]: ")
            if play_again.lower() != 'y':
                print("Goodbye!")
                break
            self.reset_game()

    def play_game(self):
        self.print_board()
        while True:

            choice = input(
                f"{self.players[self.current_player]}, {self.XorO[self.current_player]}: Enter a cell [A-C][1-3]: ")
            index = self.convert_to_index_number(choice)

            if index is not False and self.is_valid_move(index):
                self.marks[index] = self.XorO[self.current_player]
                self.print_board()  # Print the board only after a valid move
                if self.is_winner():
                    print(
                        f"{self.players[self.current_player]} is a winner!")
                    break
                elif self.is_board_full():
                    print("It is a tie!")
                    break
                else:
                    self.switch_turn()
            else:
                print("You did not choose correctly.")

    def convert_to_index_number(self, choice): #turns A,B,C into 1,2,3 then multiplies by the second number in input. EX: B2 -> 2*2 = 4. 
        if len(choice) != 2:
            return False

        column = choice[0].upper()
        row = int(choice[1])

        if column not in ['A', 'B', 'C'] or row not in [1, 2, 3]:
            return False

        column_index = ord(column) - ord('A')
        row_index = row - 1
        index = row_index * 3 + column_index
        return index

    def is_valid_move(self, index):
        if self.marks[index] == ' ':
            return True
        return False

    def is_winner(self):
        for combination in self.winning_combinations:
            if self.marks[combination[0]] == self.marks[combination[1]] == self.marks[combination[2]] != ' ':
                return True
        return False

    def is_board_full(self):
        if ' ' not in self.marks:
            return True
        return False

    def switch_turn(self):
        self.current_player = (self.current_player + 1) % 2

    def reset_game(self):
        self.marks = [' '] * 9
        self.current_player = 0

    def print_board(self):
        print(f"   A   B   C ")
        print(f" +---+---+---+")
        print(f"1| {self.marks[0]} | {self.marks[1]} | {self.marks[2]} |")
        print(f" +---+---+---+")
        print(f"2| {self.marks[3]} | {self.marks[4]} | {self.marks[5]} |")
        print(f" +---+---+---+")
        print(f"3| {self.marks[6]} | {self.marks[7]} | {self.marks[8]} |")
        print(f" +---+---+---+\n")


game = TicTacToe(['X', 'O'])
game.TTT_game()
