# Author: Olivia Choi
# GitHub username: Acos2ver
# Date: 06/02/2025
# Description: This code presents unit tests for the AnimalGame project.
# Each test function corresponds to a specific method in the game and checks its expected behavior,
# such as board setup, move validation, turn changes, and win conditions.
# All tests include docstrings that explain what each test is verifying.

import unittest
from AnimalGame import AnimalGame, Chinchilla, Wombat, Emu, Cuttlefish

class TestAnimalGame(unittest.TestCase):

    def test_init_board_setup(self):
        """
        Test if the board initializes with the correct pieces in correct starting positions.
        """
        game = AnimalGame()
        self.assertIsInstance(game._board['a1'], Chinchilla)
        self.assertIsInstance(game._board['d7'], Cuttlefish)

    def test_game_starts_unfinished(self):
        """
        Test that the initial game state is set to 'UNFINISHED'.
        """
        game = AnimalGame()
        self.assertEqual(game.get_game_state(), 'UNFINISHED')

    def test_valid_emu_move_and_turn_change(self):
        """
        Test that a valid Emu move succeeds and turn switches to AMETHYST.
        """
        game = AnimalGame()
        moved = game.make_move('c1', 'c2') # Emu moving forward
        self.assertTrue(moved)
        self.assertIsNone(game._board['c1'])
        self.assertIsInstance(game._board['c2'], Emu)
        self.assertEqual(game._turn, 'AMETHYST')

    def test_invalid_move_wrong_turn(self):
        """
        Test that a player cannot move out of turn.
        """
        game = AnimalGame()
        moved = game.make_move('c7', 'c6')     # AMETHYST's Emu moves on TANGERINE's turn
        self.assertFalse(moved)
        self.assertIsInstance(game._board['c7'], Emu)
        self.assertEqual(game._turn, 'TANGERINE')

    def test_move_to_friendly_piece_fails(self):
        """
        Ensure a player can't move onto a square occupied by their own piece.
        """
        game = AnimalGame()
        game.make_move('c1', 'c2')  # TANGERINE move
        moved = game.make_move('b7', 'a7') # AMETHYST wombat into Chinchilla
        self.assertFalse(moved)

    def test_capture_cuttlefish_ends_game(self):
        """
        Test that capturing the enemy Cuttlefish ends the game.
        """
        game = AnimalGame()
        game._board['d5'] = Cuttlefish('AMETHYST')  # manually placing cuttlefish
        game._board['d2'] = Emu('TANGERINE')        # placing Emu in range
        game._turn = 'TANGERINE'
        moved = game.make_move('d2', 'd5')
        self.assertTrue(moved)
        self.assertEqual(game.get_game_state(), 'TANGERINE_WON')

    def test_same_player_cannot_move_twice(self):
        """
        Test that the same player cannot move twice in a row.
        """
        game = AnimalGame()
        game.make_move('c1', 'c2')      # TANGERINE move
        moved = game.make_move('c2', 'c3')
        self.assertFalse(moved)
        self.assertEqual(game._turn, 'AMETHYST')

    def test_print_board_runs(self):
        """
        Confirm that print_board runs without throwing exceptions.
        """
        game = AnimalGame()
        try:
            game.print_board()
        except Exception as error:
            self.fail(str("print_board() raised an exception: {error}"))

    def test_piece_symbols(self):
        """
        Check that the correct symbols are returned for each piece.
        """
        self.assertEqual(Chinchilla("TANGERINE").symbol(), "C")
        self.assertEqual(Wombat("TANGERINE").symbol(), "W")
        self.assertEqual(Emu("TANGERINE").symbol(), "E")
        self.assertEqual(Cuttlefish("TANGERINE").symbol(), "U")

    def test_invalid_path_blocked_by_piece(self):
        """
        Test that a move is blocked if a sliding piece's path is obstructed.
        """
        game = AnimalGame()
        game._board['c2'] = Chinchilla('TANGERINE')
        moved = game.make_move('c1', 'c3')  # blocked
        self.assertFalse(moved)

if __name__ == '__main__':
    unittest.main()



