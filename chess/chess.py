from operator import indexOf
from chess.pieces import piece
from .board import Board
from .pieces.full import get_both_chess_sets

class Chess:
    
    def __init__(self):
        self.board = Board()
        self.set_up_board()
        self.board.display_board()
        
    def place_pieces(self, position, colored_set):
        row = 0 if position == 'top' else 6
        index_of = 0
        if position == 'top':
            colored_set = colored_set[::-1]
        for i in range(2):
            col = 0
            for j in range(8):
                print(row, col)
                self.board.place(colored_set[index_of], row, col)
                col += 1
                index_of += 1
            row += 1
        
    def set_up_board(self):
        pieces = get_both_chess_sets()
        print(pieces)
        white_pieces = pieces['white']
        black_pieces = pieces['black']
        self.place_pieces('bottom', white_pieces)
        self.place_pieces('top', black_pieces)
