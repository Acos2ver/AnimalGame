# Author: Olivia Choi
# GitHub username: Acos2ver
# Date: 05/30/2025
# Description: This code implements the AnimalGame, an abstract strategy board game played on
# a 7x7 grid between two players (TANGERINE and AMETHYST). Each player controls a set of
# animal-themed pieces with unique movement patterns. The goal is to capture the opponent's CUTTLEFISH.
# The game uses algebraic notation (e.g., 'a1') and include core logic and board display for testing.



class Piece:
    """
    Base class for all animal game pieces.

    Responsibilities:
    - Store the color of the piece.
    - Define the interface for validating moves

    Interacts with:
    - AnimaGame (calls is_valid_move to validate move requests).
    """

    def __init__(self, color):
        """
        Sets the color for this piece.

        Parameters:
            color (str): 'TANGERINE' or 'AMETHYST'
        """
        self._color = color

    def color(self):
        """
        Returns the color of the piece.

        Returns:
            str: 'TANGERINE' or 'AMETHYST'
        """
        return self._color

    def valid_move(self, start, end, board):
        """
        This method will be defined in each piece subclass.
        Checks if the move is allowed for the piece.
        """
        raise NotImplementedError()

    def symbol(self):
        """
        Returns the symbol for the piece.
        """
        return "?"


# Character list to replace ord/chr
COLUMNS =['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Piece subclasses with rules
class Chinchilla(Piece):
    """
    Chinchilla is a sliding piece.
    It moves exactly 1 square in any direction — orthogonal or diagonal.
    Since it's a sliding piece with a move distance of 1, it is allowed to move 1 square in all directions.
    """
    def valid_move(self, start, end, board):
        dx = abs(COLUMNS.index(start[0]) - COLUMNS.index(end[0]))   # column difference
        dy = abs(int(start[1]) - int(end[1]))   # row difference
        return max(dx, dy) == 1 # any direction one sliding

    def symbol(self):
        return "C"

class Wombat(Piece):
    """
    Wombat is a jumping piece.
    It jumps exactly 4 squares in a straight orthogonal direction (up, down, left, right),
    or it can alternatively move 1 square diagonally.
    Since it's a jumping piece, it can move either its full jump distance or take a 1-square diagonal step.
    """
    def valid_move(self, start, end, board):
        dx = abs(COLUMNS.index(start[0]) - COLUMNS.index(end[0]))
        dy = abs(int(start[1]) - int(end[1]))
        abs_dx = abs(dx)
        abs_dy = abs(dy)
        return (abs_dx == 4 and dy == 0) or (abs_dy == 4 and dx == 0) or (abs_dx == 1 and abs_dy == 1)

    def symbol(self):
        return "W"

class Emu(Piece):
    """
    Emu is a sliding piece.
    It can slide up to 3 squares in a straight orthogonal direction (horizontal or vertical),
    or move exactly 1 square diagonally.
    Since it's a sliding piece, it may move 1 square in any direction including diagonals.
    """
    def valid_move(self, start, end, board):
        dx = abs(COLUMNS.index(start[0]) - COLUMNS.index(end[0]))
        dy = abs(int(start[1]) - int(end[1]))
        if dx == 0 and 1<= dy <= 3:
            return True
        if dy == 0 and 1<= dx <= 3:
            return True
        if dx == 1 and dy == 1:
            return True
        return False

    def symbol(self):
        return "E"

class Cuttlefish(Piece):
    """
    Cuttlefish is a jumping piece.
    It jumps exactly 2 squares diagonally, or can alternatively move 1 square orthogonally.
    If a Cuttlefish is captured, the game ends immediately.
    """
    def valid_move(self, start, end, board):
        dx = abs(COLUMNS.index(start[0]) - COLUMNS.index(end[0]))
        dy = abs(int(start[1]) - int(end[1]))
        return (dx == 2 and dy == 2) or (dx == 1 and dy == 0) or (dx == 0 and dy == 1)

    def symbol(self):
        return "U"

# Main game controller
class AnimalGame:
    """
    Main class (game state, board setup, and player turns) for controlling the AnimalGame.

    Responsibilities:
    - Maintain board state, player turns, and game status.
    - Validate and apply legal moves.
    - Detect win condition (Cuttlefish capture).
    """
    def __init__(self):
        """
        Initializes the game by setting up the board, turn, and state.
        """
        self._board = {}                    # Dictionary of positions to piece instances
        self._game_state = 'UNFINISHED'     # Current game state
        self._turn = 'TANGERINE'            # Starting player
        self._place_initial_pieces()            # Populate initial piece

    def _place_initial_pieces(self):
        """
        Set up a 7x7 board with each player's pieces on their respective rows.
        """
        row_order = ['chinchilla', 'wombat', 'emu', 'cuttlefish', 'emu', 'wombat', 'chinchilla']
        for index, name in enumerate(row_order):
            # Place TANGERINE pieces on row 1 (bottom)
            self._board[COLUMNS[index] + '1'] = self._create_piece(name, 'TANGERINE')
            # Place AMETHYST pieces on row 7 (top)
            self._board[COLUMNS[index] + '7'] = self._create_piece(name, 'AMETHYST')

    def _create_piece(self, name, color):
        """
        Create and return a piece object based on name and color.

        Parameters:
            name (str): Type of the piece
            color (str): 'TANGERINE' or 'AMETHYST'

        Returns:
            piece: Corresponding piece instance
        """
        if name == 'chinchilla':
            return Chinchilla(color)
        elif name == 'wombat':
            return Wombat(color)
        elif name == 'emu':
            return Emu(color)
        elif name == 'cuttlefish':
            return Cuttlefish(color)

    def get_game_state(self):
        """
        Returns the current state of the game.

        Returns:
            str: 'UNFINISHED', 'TANGERINE_WON', or 'AMETHYST_WON'
        """
        return self._game_state

    def make_move(self, start, end):
        """
        Attempt to move a piece from start to end.
        Returns True if successful.
        Invalid moves return False.

        Parameters:
            start (str): Starting square (e.g., 'a1')
            end (str): Destination square (e.g., 'a2')

        Returns:
            bool: True if move was successful, False otherwise
        """
        if self._game_state != 'UNFINISHED':
            return False

        if start not in self._board or self._board[start] is None:
            return False

        piece = self._board[start]

        if piece.color() != self._turn:
            return False

        if not piece.valid_move(start, end, self._board):
            return False

        target = self._board.get(end)
        if target and target.color() == self._turn:
            return False        # Cannot move onto a friendly piece

        # If sliding piece exists, check the path
        if isinstance(piece, Emu) or isinstance(piece, Chinchilla):
            if not self._path_clear(start, end):
                return False

        # Check for win condition
        if isinstance(target, Cuttlefish):
            self._game_state = 'TANGERINE_WON' if target.color() == 'AMETHYST' else 'AMETHYST_WON'

        self._board[end] = piece        # Move piece to destination
        self._board[start] = None       # Clear start square
        self._turn = 'AMETHYST' if self._turn == 'TANGERINE' else 'TANGERINE'
        return True

    def _path_clear(self, start, end):
        """
        Check if sliding movement path is clear of other pieces.
        Only used by Emu and Chinchilla.
        """
        column_start = COLUMNS.index(start[0])
        row_start = int(start[1])
        column_end = COLUMNS.index(end[0])
        row_end = int(end[1])

        dx = column_end - column_start
        dy = row_end  - row_start

        # Determine direction
        step_column = 0 if dx == 0 else (1 if dx > 0 else -1)
        step_row = 0 if dy == 0 else (1 if dy > 0 else -1)

        column = column_start + step_column
        row = row_start + step_row

        while column != column_end or row != row_end:
            position = COLUMNS[column] + str(row)
            if self._board.get(position) is not None:
                return False
            column += step_column
            row += step_row

        return True

    def print_board(self):
        """
        Prints the current state of the board for debugging.
        """
        for row in range(7, 0, -1):
            line = str(row) + " "
            for column in range(7):
                square = COLUMNS[column] + str(row)
                piece = self._board.get(square)
                if piece:
                    line += piece.symbol() + " "
                else:
                    line += ". "
            print(line)
        print("  a b c d e f g")

# if __name__=="__main__":
#    game = AnimalGame()
#    print("__Initial Board__")
#    game.print_board()
#    print()

#    print("[Move] TANGERINE:c1 -> c2")
#    move_result = game.make_move('c1', 'c2')
#    print("Move result:", move_result)
#    print()

#    print("__Board After Move__")
#    game.print_board()
#    print()

#   state = game.get_game_state()
#    print("Game State:", state)
