from simpleTTT import Board
import unittest
from constants import FIRST_PLAYER, SECOND_PLAYER, INVALID_MOVE_MESSAGE, TAKEN_SQUARE_MESSAGE, DRAW_MESSAGE

class TestFunction(unittest.TestCase):
    def test_empty_board(self):
        empty_board = Board()
        self.assertEqual(empty_board.board, 
                        [[None, None, None], [None, None, None], [None, None, None]]   
                         )

    def test_plot_middle(self):
        plot_middle = Board()
        plot_middle.move(1, 1, plot_middle.player)
        self.assertEqual(plot_middle.board, 
                        [[None, None, None], [None, 'X', None], [None, None, None]]
                         )
        
    def test_X_win_row(self):
        X_win = Board()
        X_win.move(1, 0, X_win.player)
        X_win.move(0, 0, X_win.player)
        X_win.move(1, 1, X_win.player)
        X_win.move(2, 1, X_win.player)
        X_win.move(1, 2, X_win.player)
        self.assertEqual(X_win.winner, FIRST_PLAYER)
    
    def test_O_win_row(self):
        O_win = Board()
        O_win.move(1, 0, O_win.player)
        O_win.move(0, 0, O_win.player)
        O_win.move(1, 2, O_win.player)
        O_win.move(0, 1, O_win.player)
        O_win.move(2, 1, O_win.player)
        O_win.move(0, 2, O_win.player)
        self.assertEqual(O_win.winner, SECOND_PLAYER)

    def test_X_win_col(self):
        X_win = Board()
        X_win.move(0, 0, X_win.player)
        X_win.move(0, 1, X_win.player)
        X_win.move(1, 0, X_win.player)
        X_win.move(2, 1, X_win.player)
        X_win.move(2, 0, X_win.player)
        self.assertEqual(X_win.winner, FIRST_PLAYER)

    def test_O_win_col(self):
        O_win = Board()
        O_win.move(0, 1, O_win.player)
        O_win.move(0, 0, O_win.player)
        O_win.move(0, 2, O_win.player)
        O_win.move(1, 0, O_win.player)
        O_win.move(2, 2, O_win.player)
        O_win.move(2, 0, O_win.player)
        self.assertEqual(O_win.winner, SECOND_PLAYER)

    def test_X_win_diag(self):
        X_win = Board()
        X_win.move(0, 0, X_win.player)
        X_win.move(0, 1, X_win.player)
        X_win.move(1, 1, X_win.player)
        X_win.move(2, 1, X_win.player)
        X_win.move(2, 2, X_win.player)
        self.assertEqual(X_win.winner, FIRST_PLAYER)

    def test_O_win_diag(self):
        O_win = Board()
        O_win.move(0, 1, O_win.player)
        O_win.move(1, 1, O_win.player)
        O_win.move(1, 0, O_win.player)
        O_win.move(2, 0, O_win.player)
        O_win.move(2, 2, O_win.player)
        O_win.move(0, 2, O_win.player)
        self.assertEqual(O_win.winner, SECOND_PLAYER)

    def test_draw(self):
        draw = Board()
        draw.move(1, 1, draw.player)
        draw.move(0, 0, draw.player)
        draw.move(2, 2, draw.player)
        draw.move(2, 1, draw.player)
        draw.move(1, 0, draw.player)
        draw.move(1, 2, draw.player)
        draw.move(0, 2, draw.player)
        draw.move(2, 0, draw.player)
        draw.move(0, 1, draw.player)
        self.assertEqual(draw.winner, '')



if __name__ == '__main__':
    unittest.main()