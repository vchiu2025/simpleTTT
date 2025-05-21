from simpleTTT import Board
import random
from constants import DRAW_MESSAGE, RESTART
from minimax import get_best_move


class GameMode:
    def __init__(self):
        self.board = Board()

    def prompt_move(self) -> str:
        return input(
            "Give a coordinate in the form x,y to make a move. \n(type 'restart' to restart the game) "
        )

    def handle_moves(self, move_str: str) -> None:
        try:
            if move_str.lower() == RESTART:
                self.board.reset()
            else:
                moves_lst = move_str.split(",")
                x_coord = int(moves_lst[0].strip())
                y_coord = int(moves_lst[1].strip())
                if not self.board.is_move_invalid(x_coord, y_coord):
                    self.board.move(x_coord, y_coord, self.board.player)
                    self.make_ai_move()
        except Exception as e:
            print(f"Invalid input: {e}")
        self.print_board()

    def print_board(self) -> None:
        print(self.board)

    def handle_game_end(self) -> None:
        if not self.board.winner:
            print(DRAW_MESSAGE)
        else:
            self.board.switch_players()
            print(self.board.player, " Wins!")

    def play(self) -> None:
        self.print_board()
        while not self.board.is_game_over:
            human_input = self.prompt_move()
            self.handle_moves(human_input)
        self.handle_game_end()

    def make_ai_move(self) -> None:
        raise NotImplementedError("Subclasses must implement make_move()")


class DumbBotGame(GameMode):
    def make_ai_move(self):
        if not self.board.is_game_over:
            ai_move = random.choice(self.board.possible_moves)
            ai_x_coord, ai_y_coord = ai_move[0], ai_move[1]
            self.board.move(ai_x_coord, ai_y_coord, self.board.player)
            print(f"Dumb Bot's move was {ai_x_coord}, {ai_y_coord}.")


class SmartBotGame(GameMode):
    def make_ai_move(self):
        if not self.board.is_game_over:
            smart_bot = self.board.player
            smart_ai_move = get_best_move(self.board, smart_bot)
            if smart_ai_move:
                ai_x, ai_y = smart_ai_move
                self.board.move(ai_x, ai_y, smart_bot)
                print(f"Smart Bot's move was {ai_x}, {ai_y}.")


class PvPGame(GameMode):
    def make_ai_move(self):
        return
