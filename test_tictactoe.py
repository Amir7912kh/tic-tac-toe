import unittest
import tictactoe

class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        """Reset the board before each test."""
        tictactoe.board = [[' ' for _ in range(3)] for _ in range(3)]

    def test_check_win_row(self):
        """Test win condition in a row."""
        tictactoe.board[0] = ['X', 'X', 'X']
        self.assertTrue(tictactoe.check_win('X'))

    def test_check_win_col(self):
        """Test win condition in a column."""
        for i in range(3):
            tictactoe.board[i][0] = 'O'
        self.assertTrue(tictactoe.check_win('O'))

    def test_check_win_diag(self):
        """Test win condition in a diagonal."""
        for i in range(3):
            tictactoe.board[i][i] = 'X'
        self.assertTrue(tictactoe.check_win('X'))

    def test_check_no_win(self):
        """Test a non-winning board."""
        tictactoe.board[0] = ['X', 'O', 'X']
        self.assertFalse(tictactoe.check_win('X'))
        self.assertFalse(tictactoe.check_win('O'))

    def test_check_draw(self):
        """Test a draw condition."""
        tictactoe.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        self.assertTrue(tictactoe.check_draw())

    def test_check_not_draw(self):
        """Test a non-draw board."""
        tictactoe.board[0][0] = 'X'
        self.assertFalse(tictactoe.check_draw())

    def test_ai_wins(self):
        """Test if AI makes a winning move."""
        tictactoe.board[0] = ['O', 'O', ' ']
        tictactoe.board[1] = ['X', 'X', ' ']
        tictactoe.board[2] = [' ', ' ', ' ']
        tictactoe.ai_move()
        self.assertEqual(tictactoe.board[0][2], 'O')

    def test_ai_blocks(self):
        """Test if AI blocks a player's winning move."""
        tictactoe.board[0] = ['X', 'X', ' ']
        tictactoe.board[1] = ['O', ' ', ' ']
        tictactoe.board[2] = ['O', ' ', ' ']
        tictactoe.ai_move()
        self.assertEqual(tictactoe.board[0][2], 'O')

if __name__ == '__main__':
    unittest.main()
