class Board():
    def __init__(self):
        self.player = "X"
        self.rows = 3
        self.cols = 3
        self.board = [[None for i in range(self.cols)] for _ in range(self.rows)]
        self.num_moves = 0
        self.is_game_over = False


    def move(self, x, y, p):
        if not 0 <= x < self.rows or not 0 <= y < self.cols:
            print("Invalid move dumbass.")
            return
        if self.board[x][y]: 
            print("This square is already taken idiot.")
            return

        self.board[x][y] = p
        print(self)

        # if every row or column is occupied by the same player, game ends
        for i in range(len(self.board)):
            row = self.board[i]
            col = [self.board[i][j] for j in range(self.cols)]

            if all(a == self.player for a in row) or all(b == self.player for b in col):
                print(self.player + " Wins!")
                self.is_game_over = True
                self.reset()

        # if the diagonals are occupied by the same player, game ends
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.player:
            print(self.player + " Wins!")
            self.is_game_over = True
            self.reset()
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.player:
            print(self.player + " Wins!")
            self.is_game_over = True
            self.reset()
            
        # switch players
        if self.player == "X":
            self.player = "O"
        elif self.player == "O":
            self.player = "X"
        
        

        self.num_moves += 1
        # if every square is taken, game ends
        if self.num_moves >= self.rows * self.cols:
            print("its a draw, you guys are equally dumb")
            self.is_game_over = True
            self.reset()
        
    def __str__(self):
        symbols = {None: ' ', 'X': 'X', 'O': 'O'}
        rows = [' | '.join(symbols[cell] for cell in row) for row in self.board]
        return '\n---------\n'.join(rows)
        
    def __repr__(self):
        symbols = {None: ' ', 'X': 'X', 'O': 'O'}
        rows = []
        for row in self.board:
            rows.append(' | '.join(symbols[cell] for cell in row))
        return '\n---------\n'.join(rows)
    

    # clear the board
    def reset(self):
        self.matrix = [[None for i in range(self.cols)] for _ in range(self.rows)]



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