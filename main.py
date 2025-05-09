from simpleTTT import Board

def main():
    board = Board()
    while not board.is_game_over:
        moves = input("Give a coordinate in the form x,y to make a move: ")
        try:
            moves_lst = moves.split(",")
            x_coord = int(moves_lst[0].strip())
            y_coord = int(moves_lst[1].strip())
            board.move(x_coord, y_coord, board.player)
        except Exception as e:
            print(e)
            

if __name__ == "__main__":
    main()