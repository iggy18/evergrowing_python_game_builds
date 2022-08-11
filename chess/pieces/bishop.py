from .piece import Piece

class Bishop(Piece):
    
    #can move and attack diagonally in any direction
    #can move any number of squares
    #can not jump over other pieces
    
    def __init__(self):
        super().__init__()
        self.set_name("B")