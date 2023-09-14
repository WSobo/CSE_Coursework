import numpy as np


class Fifteen:

    # create a vector (ndarray) of tiles and the layout of tiles positions (a graph)
    # tiles are numbered 1-15, the last tile is 0 (an empty space)
    def __init__(self, size=4):
        self.size = size
        self.tiles = np.array([i for i in range(1, size**2)] + [0])
        self.layout = np.reshape(self.tiles, (size, size))

    # draw the layout with tiles:
    # +---+---+---+---+
    # | 1 | 2 | 3 | 4 |
    # +---+---+---+---+
    # | 5 | 6 | 7 | 8 |
    # +---+---+---+---+
    # | 9 |10 |11 |12 |
    # +---+---+---+---+
    # |13 |14 |15 |   |
    # +---+---+---+---+
    def draw(self):
        for row in self.layout:
            print("+---" * self.size + "+")
            print("|", end="")
            for tile in row:
                if tile == 0:
                    print("   |", end="")
                else:
                    print(f" {tile} |", end="")
            print()
        print("+---" * self.size + "+")

    # return a string representation of the vector of tiles as a 2d array
    # 1  2  3  4
    # 5  6  7  8
    # 9 10 11 12
    # 13 14 15
    def __str__(self):
        return str(np.reshape(self.tiles, (self.size, self.size)))

    # exchange i-tile with j-tile
    # tiles are numbered 1-15, the last tile is 0 (empty space)
    # the exchange can be done using a dot product (not required)
    # can return the dot product (not required)
    def transpose(self, i, j):
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]

    # checks if the move is valid: one of the tiles is 0 and another tile is its neighbor
    def is_valid_move(self, move):
        zero_index = np.where(self.tiles == 0)[0][0]
        move_index = np.where(self.tiles == move)[0][0]

        zero_row, zero_col = self.get_empty_space_position()
        move_row, move_col = move_index // self.size, move_index % self.size

        # Check if the move tile is adjacent to the empty space
        return (
            (zero_row == move_row and abs(zero_col - move_col) == 1) or
            (zero_col == move_col and abs(zero_row - move_row) == 1)
        )

    def move_tile(self, row, col):
        empty_index = np.where(self.tiles == 0)[0][0]
        move_index = row * self.size + col
        if self.is_valid_move(self.tiles[move_index]):
            self.transpose(empty_index, move_index)

    # update the vector of tiles
    # if the move is valid assign the vector to the return of transpose() or call transpose
    def update(self, move):
        if self.is_valid_move(move):
            zero_index = np.where(self.tiles == 0)[0][0]
            move_index = np.where(self.tiles == move)[0][0]
            self.transpose(zero_index, move_index)

    # shuffle tiles
    def shuffle(self, moves=100):
        for _ in range(moves):
            valid_moves = [
                tile for tile in self.tiles if self.is_valid_move(tile)]
            random_move = np.random.choice(valid_moves)
            self.update(random_move)

    def is_solved(self):
        return np.array_equal(self.tiles[:-1], np.arange(1, self.size**2))

    def is_solvable(self):
        inv_count = 0
        for i in range(len(self.tiles)):
            for j in range(i + 1, len(self.tiles)):
                if self.tiles[i] and self.tiles[j] and self.tiles[i] > self.tiles[j]:
                    inv_count += 1
        return inv_count % 2 == 0

    def get_empty_space_position(self):
        zero_index = np.where(self.tiles == 0)[0][0]
        row = zero_index // self.size
        col = zero_index % self.size
        return row, col
