from .square import ChessBoardSquare

class Board:
    
    def __init__(self):
        self.board = [[ChessBoardSquare() for x in range(8)] for y in range(8)]
        
    def display_boarder(self, position):
        bottom = "    a b c d e f g h"
        boarder = "   -----------------"
        if position == "top":
            print(boarder)
        if position == "bottom":    
            print(boarder)
            print(bottom)
        
    def display_board(self):
        number = 1
        self.display_boarder("top")
        for row in self.board:
            print('{}{}| {} |'.format(number,' ', ' '.join(str(x) if x is not None else str(0) for x in row)))
            number += 1
        self.display_boarder("bottom")
        
    def place(self, piece, rank, file):
        self.board[rank][file].set_piece(piece)