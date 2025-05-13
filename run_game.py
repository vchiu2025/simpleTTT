from simpleTTT import Board
import random
from constants import Player, DRAW_MESSAGE
from typing import Optional, Tuple


def play_dumb_bot():
    print("You're now playing Dumb Bot. \n")
    # DUMB 'AI' FEATURE (just chooses squares randomly)
    board = Board()
    print(board)
    while not board.is_game_over:
        moves = input(
            "Give a coordinate in the form x,y to make a move. \n(type 'restart' to restart the game) "
        )
        try:
            if moves == "restart":
                board.reset()
            else:
                # human move
                moves_lst = moves.split(",")
                x_coord = int(moves_lst[0].strip())
                y_coord = int(moves_lst[1].strip())
                if not board.is_move_invalid(x_coord, y_coord):
                    board.move(x_coord, y_coord, board.player)

                    # dumb ai move
                    if not board.is_game_over:
                        ai_move = random.choice(board.possible_moves)
                        ai_x_coord = ai_move[0]
                        ai_y_coord = ai_move[1]
                        board.move(ai_x_coord, ai_y_coord, board.player)
                        print(f"Dumb Bot's move was {ai_x_coord}, {ai_y_coord}.")
                else:
                    continue
            print(board)
        except Exception as e:
            print(e)
    if not board.winner:
        print(DRAW_MESSAGE)
    else:
        board.switch_players()
        print(board.player, " Wins!")


def play_smart_bot():
    print("You're now playing Smart Bot. \n")
    # A SMART AI FEATURE (MINIMAX ALGORITHM)
    board = Board()
    print(board)
    while not board.is_game_over:
        moves = input(
            "Give a coordinate in the form x,y to make a move. \n(type 'restart' to restart the game) "
        )
        try:
            if moves == "restart":
                board.reset()
            else:
                # human move
                moves_lst = moves.split(",")
                x_coord = int(moves_lst[0].strip())
                y_coord = int(moves_lst[1].strip())
                if not board.is_move_invalid(x_coord, y_coord):
                    board.move(x_coord, y_coord, board.player)

                    # smart ai move
                    if not board.is_game_over:
                        smart_bot = board.player
                        smart_ai_move = get_best_move(board, smart_bot)
                        if smart_ai_move:
                            ai_x, ai_y = smart_ai_move
                            board.move(ai_x, ai_y, smart_bot)
                            print(f"Smart Bot's move was {ai_x}, {ai_y}.")
                else:
                    continue
            print(board)
        except Exception as e:
            print(e)
    if not board.winner:
        print(DRAW_MESSAGE)
    else:
        board.switch_players()
        print(board.player, " Wins!")


def play_pvp():
    board = Board()
    print(board)
    print("Player 1 (X) goes first.")
    while not board.is_game_over:
        moves = input(
            "Give a coordinate in the form x,y to make a move. \n(type 'restart' to restart the game) "
        )
        try:
            if moves == "restart":
                board.reset()
            else:
                moves_lst = moves.split(",")
                x_coord = int(moves_lst[0].strip())
                y_coord = int(moves_lst[1].strip())
                board.move(x_coord, y_coord, board.player)
                print(board)
        except Exception as e:
            print(e)
    if not board.winner:
        print(DRAW_MESSAGE)
    else:
        board.switch_players()
        print(board.player, " Wins!")


def minimax(
    board: Board, is_maximizing: bool, bot_player: Player, depth: int = 0
) -> int:
    if bot_player == Player.FIRST:
        opponent = Player.SECOND
    else:
        opponent = Player.FIRST

    if board.is_game_over:
        if board.winner == bot_player:
            return 10 - depth
        elif board.winner == opponent:
            return depth - 10
        else:
            return 0

    if is_maximizing:
        best_score = float("-inf")
        current_player = bot_player
    else:
        best_score = float("inf")
        current_player = opponent

    for x in range(3):
        for y in range(3):
            if board.board[x][y] is None:
                board.move(x, y, current_player)
                score = minimax(board, not is_maximizing, bot_player, depth + 1)
                board.undo_move(x, y)
                if is_maximizing:
                    best_score = max(score, best_score)
                else:
                    best_score = min(score, best_score)

    return best_score


def get_best_move(board: Board, bot_player: Player) -> Optional[Tuple[int, int]]:
    best_score = float("-inf")
    best_move = None

    for x in range(3):
        for y in range(3):
            if board.board[x][y] is None:
                board.move(x, y, bot_player)
                score = minimax(board, False, bot_player, depth=1)
                board.undo_move(x, y)
                if score > best_score:
                    best_score = score
                    best_move = (x, y)

    return best_move
