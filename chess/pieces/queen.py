from .piece import Piece

class Queen(Piece):
    
    #can move any number of squares in any direction
    #can not jump over other pieces
    
    def __init__(self):
        super().__init__()
        self.set_name("Q")