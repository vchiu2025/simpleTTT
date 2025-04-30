from constants import FIRST_PLAYER, SECOND_PLAYER, INVALID_MOVE_MESSAGE, TAKEN_SQUARE_MESSAGE, DRAW_MESSAGE

class Board():
    "Represents the classic 3x3 Tic Tac Toe Board"

    def __init__(self, rows=3, cols=3):
        self.player: str = FIRST_PLAYER
        self.rows: int = rows
        self.cols: int = cols
        self.board: str = [[None for i in range(self.cols)] for _ in range(self.rows)]
        self.num_moves: int = 0
        self.is_game_over: bool = False
        self.winner: str = ''


    def move(self, x_coordinate: int, y_coordinate:int , player: str) -> None:

        WINNING_MESSAGE = self.player + " WINS!"

        if not 0 <= x_coordinate < self.rows or not 0 <= y_coordinate < self.cols:
            print(INVALID_MOVE_MESSAGE)
            return
        if self.board[x_coordinate][y_coordinate]: 
            print(TAKEN_SQUARE_MESSAGE)
            return

        self.board[x_coordinate][y_coordinate] = player
        print(self)
        self.num_moves += 1

        if self.has_player_won():
            print(WINNING_MESSAGE)
            self.winner = self.player
            self.is_game_over = True
            self.reset()
        
        elif self.is_draw():
            print(DRAW_MESSAGE)
            self.is_game_over = True
            self.reset()

        self.switch_players() 


    def is_draw(self) -> bool:
        # if every square is taken, game ends
        if self.num_moves >= self.rows * self.cols:
            return True
        else:
            return False


    def has_player_won(self) -> bool:
        # if a whole row or column is occupied by the same player, game ends
        for i in range(len(self.board)):
            row = self.board[i]
            col = [self.board[j][i] for j in range(self.cols)]
            if all(a == self.player for a in row) or all(b == self.player for b in col):
                return True

        # if one of the diagonals are occupied by the same player, game ends
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player:
            return True
        
        return False


        
    def switch_players(self) -> None:
        if self.player == FIRST_PLAYER:
            self.player = SECOND_PLAYER
        elif self.player == SECOND_PLAYER:
            self.player = FIRST_PLAYER


    def __str__(self):
        symbols = {None: ' ', FIRST_PLAYER: FIRST_PLAYER, SECOND_PLAYER: SECOND_PLAYER}
        rows = [' | '.join(symbols[cell] for cell in row) for row in self.board]
        return '\n---------\n'.join(rows)
        
    def __repr__(self):
        return self.__str__()
    

    def reset(self) -> None:
        self.matrix = [[None for i in range(self.cols)] for _ in range(self.rows)]