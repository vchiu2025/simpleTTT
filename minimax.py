from constants import Player
from simpleTTT import Board
from typing import Optional, Tuple

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
