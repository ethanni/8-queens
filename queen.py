class queens:
    def __init__(self, size):
        self.size = size

    def print_board(self, board, size):
        for i in range(size):
            for j in range(size):
                print(board[i][j], end=' ')
            print()

    def is_valid(self, board, row, col, size):
        # check to see if queen is already in the row
        for i in range(col):
            if board[row][i] == "Q":
                return False
        # check diagonal going from bottom left to top right
        for i, j in zip(range(row, size, 1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False
        # check diagonal going from top left to bottom right
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == "Q":
                return False
        return True

    def solve(self, board, col, size):
        if col >= size:  # all queens have been placed
            return True

        for i in range(size):
            if self.is_valid(board, i, col, size):
                board[i][col] = "Q"

                if self.solve(board, col + 1, size):  # try to the the queen in the next spot
                    return True

                board[i][col] = "-"  # queen cannot be put in that spot

        return False

    def start_solve(self, size):
        board = [["-"] * size for i in range(size)]
        if not self.solve(board, 0, size):
            print("No solution")

        self.print_board(board, size)