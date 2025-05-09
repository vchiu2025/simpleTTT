from simpleTTT import Board
import random


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
                moves_lst = moves.split(",")
                x_coord = int(moves_lst[0].strip())
                y_coord = int(moves_lst[1].strip())
                board.move(x_coord, y_coord, board.player)
                board.possible_moves.remove([x_coord, y_coord])

                # dumb ai move
                if not board.is_game_over:
                    ai_move = random.choice(board.possible_moves)
                    board.possible_moves.remove(ai_move)
                    ai_x_coord = ai_move[0]
                    ai_y_coord = ai_move[1]
                    board.move(ai_x_coord, ai_y_coord, board.player)
                    print(f"Dumb Bot's move was {ai_x_coord}, {ai_y_coord}.")
        except Exception as e:
            print(e)


def play_smart_bot():
    print("You're now playing Smart Bot. \n")
    # MAKE A SMART AI FEATURE (MINIMAX ALGORITHM)
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
                moves_lst = moves.split(",")
                x_coord = int(moves_lst[0].strip())
                y_coord = int(moves_lst[1].strip())
                board.move(x_coord, y_coord, board.player)
        except Exception as e:
            print(e)


def play_pvp():
    board = Board()
    print(board)
    while not board.is_game_over:
        moves = input(
            "Player 1 (X) goes first. Give a coordinate in the form x,y to make a move. \n(type 'restart' to restart the game) "
        )
        try:
            if moves == "restart":
                board.reset()
            else:
                moves_lst = moves.split(",")
                x_coord = int(moves_lst[0].strip())
                y_coord = int(moves_lst[1].strip())
                board.move(x_coord, y_coord, board.player)
        except Exception as e:
            print(e)
