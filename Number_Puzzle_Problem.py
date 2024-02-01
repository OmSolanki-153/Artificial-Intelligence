import random

class Puzzle:
    def __init__(self):
        self.grid = [[0, 0, 0],
                     [0, 0, 0],
                     [0, 0, 0]]
        self.empty_row = 0
        self.empty_col = 0
        self.generate_puzzle()

    def generate_puzzle(self):
        nums = list(range(1, 9))
        random.shuffle(nums)
        nums_iter = iter(nums)
        for i in range(3):
            for j in range(3):
                if i == 2 and j == 2:
                    self.grid[i][j] = 0
                    self.empty_row = i
                    self.empty_col = j
                else:
                    self.grid[i][j] = next(nums_iter)

    def print_puzzle(self):
        for row in self.grid:
            print(row)

    def move_tile(self, direction):
        if direction == 'up' and self.empty_row < 2:
            self.grid[self.empty_row][self.empty_col], self.grid[self.empty_row + 1][self.empty_col] = \
                self.grid[self.empty_row + 1][self.empty_col], self.grid[self.empty_row][self.empty_col]
            self.empty_row += 1
        elif direction == 'down' and self.empty_row > 0:
            self.grid[self.empty_row][self.empty_col], self.grid[self.empty_row - 1][self.empty_col] = \
                self.grid[self.empty_row - 1][self.empty_col], self.grid[self.empty_row][self.empty_col]
            self.empty_row -= 1
        elif direction == 'left' and self.empty_col < 2:
            self.grid[self.empty_row][self.empty_col], self.grid[self.empty_row][self.empty_col + 1] = \
                self.grid[self.empty_row][self.empty_col + 1], self.grid[self.empty_row][self.empty_col]
            self.empty_col += 1
        elif direction == 'right' and self.empty_col > 0:
            self.grid[self.empty_row][self.empty_col], self.grid[self.empty_row][self.empty_col - 1] = \
                self.grid[self.empty_row][self.empty_col - 1], self.grid[self.empty_row][self.empty_col]
            self.empty_col -= 1

# Example usage:
if __name__ == "__main__":
    puzzle = Puzzle()
    print("Initial Puzzle:")
    puzzle.print_puzzle()
    print("\nMoving up:")
    puzzle.move_tile('up')
    puzzle.print_puzzle()
    print("\nMoving down:")
    puzzle.move_tile('down')
    puzzle.print_puzzle()
    print("\nMoving left:")
    puzzle.move_tile('left')
    puzzle.print_puzzle()
    print("\nMoving right:")
    puzzle.move_tile('right')
    puzzle.print_puzzle()
