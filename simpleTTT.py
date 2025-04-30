class Board():
    def __init__(self):
        self.player = "X"
        self.rows = 3
        self.cols = 3
        self.board = [[None for i in range(self.cols)] for _ in range(self.rows)]
        self.num_moves = 0
        self.is_game_over = False