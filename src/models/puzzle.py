import random
import itertools

class Puzzle:
    """
    A class representing an '8-puzzle'.
    - 'board' should be a square list of lists with integer entries
       e.g. [[1,2,3],[4,0,6],[7,5,8]]
    """
    def __init__(self, board):
        self.width = len(board[0])
        self.board = board

    @property
    def solved(self):
        """
        The puzzle is solved if the flattened board's numbers are in
        increasing order from left to right and the '0' tile is in the
        last position on the board
        """
        N = self.width * self.width

        return str(self) == ''.join(map(str, range(1, N))) + '0'

    @property
    def actions(self):
        """
        Return a list of 'move', 'action' pairs. 'move' can be called
        to return a new puzzle that results in sliding the '0' tile in
        the direction of 'action'.
        """
        def create_move(at, to):
            return lambda: self._move(at, to)

        moves = []

        for i , j in itertools.product(range(self.width), range(self.width)):
            direcs = {
              'Right': (i, j - 1),
              'Left': (i, j + 1),
              'Down': (i - 1, j),
              'Up': (i + 1, j)
            }

            for action, (row, column) in direcs.items():
                if row >= 0 and column >= 0 and row < self.width and column < self.width and self.board[row][column] == 0:
                    move = create_move((i, j), (row, column)), action
                    moves.append(move)

        return moves

    @property
    def manhattan(self):
        distance = 0

        for row in range(3):
            for column in range(3):
                if self.board[row][column] != 0:
                    x, y = divmod(self.board[row][column] - 1, 3)
                    distance += abs(x - row) + abs(y - column)

        return distance

    def shuffle(self):
        """
        Return a new puzzle that has been shuffled with 1000 random moves
        """
        puzzle = self

        for _ in range(1000):
            puzzle = random.choice(puzzle.actions)[0]()

        return puzzle

    def copy(self):
        """
        Return a new puzzle with the same board as 'self'
        """
        board = []

        for row in self.board:
            board.append([x for x in row])

        return Puzzle(board)

    def _move(self, at, to):
        """
        Return a new puzzle where 'at' and 'to' tiles have been swapped. All moves should be actions that have been executed
        """
        copy = self.copy()
        at_row, at_column = at
        to_row, to_column = to

        copy.board[at_row][at_column], copy.board[to_row][to_column] = copy.board[to_row][to_column], copy.board[at_row][at_column]

        return copy

    def print_puzzle(self):
        for row in self.board:
            print(row)

        print()

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        for row in self.board:
            yield from row