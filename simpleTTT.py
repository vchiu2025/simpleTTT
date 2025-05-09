from constants import (
    INVALID_MOVE_MESSAGE,
    TAKEN_SQUARE_MESSAGE,
    DRAW_MESSAGE,
    POSSIBLE_MOVES,
)
from constants import Player


class Board:
    "Represents the classic 3x3 Tic Tac Toe Board"

    def __init__(self):
        self.player: str = Player.FIRST
        self.rows: int = 3
        self.cols: int = 3
        self.board: str = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.num_moves: int = 0
        self.is_game_over: bool = False
        self.winner: str = None
        self.possible_moves = POSSIBLE_MOVES[:]

    def move(self, x_coordinate: int, y_coordinate: int, player: str) -> None:
        if self.is_move_invalid(x_coordinate, y_coordinate):
            return

        self.make_move(x_coordinate, y_coordinate, player)

        if self.has_player_won():
            self.end_game_win()

        elif self.is_draw():
            self.end_game_draw()

        self.switch_players()

    def make_move(self, x_coordinate: int, y_coordinate: int, player: str) -> None:
        self.board[x_coordinate][y_coordinate] = player
        print(self)
        self.num_moves += 1

    def end_game_win(self) -> None:
        winning_message = f"GOOD JOB, {self.player} WINS!"
        print(winning_message)
        self.winner = self.player
        self.is_game_over = True

    def end_game_draw(self) -> None:
        print(DRAW_MESSAGE)
        self.is_game_over = True

    def is_move_invalid(self, x_coordinate: int, y_coordinate: int) -> bool:
        if not 0 <= x_coordinate < self.rows or not 0 <= y_coordinate < self.cols:
            print(INVALID_MOVE_MESSAGE)
            return True

        if self.board[x_coordinate][y_coordinate]:
            print(TAKEN_SQUARE_MESSAGE)
            return True

        return False

    def is_draw(self) -> bool:
        # if every square is taken, game ends

        return self.num_moves >= self.rows * self.cols

    def has_player_won(self) -> bool:
        # if a whole row or column is occupied by the same player, game ends
        for i in range(len(self.board)):
            row = self.board[i]
            col = [self.board[j][i] for j in range(self.cols)]
            if all(a == self.player for a in row) or all(b == self.player for b in col):
                return True

        # if one of the diagonals are occupied by the same player, game ends
        return (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player
            or self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player
        )

    def switch_players(self) -> None:
        player_map = {Player.FIRST: Player.SECOND, Player.SECOND: Player.FIRST}
        self.player = player_map[self.player]

    def __str__(self):
        symbols = {None: " ", Player.FIRST: Player.FIRST, Player.SECOND: Player.SECOND}
        rows = [" | ".join(symbols[cell] for cell in row) for row in self.board]
        return "\n---------\n".join(rows)

    def __repr__(self):
        return self.__str__()

    def reset(self) -> None:
        self.board: str = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.num_moves = 0
        print(self)
        self.possible_moves = POSSIBLE_MOVES[:]
