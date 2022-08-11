from .piece import Piece

class Rook(Piece):
    #can move horizontally or vertically in any direction
    #can move any number of squares
    #can not jump over other pieces
    
    def __init__(self):
        super().__init__()
        self.set_name("R")