from .piece import Piece

class Knight(Piece):
    
    # can move and attack 
    # can move in an L-shape
    # can jump over other pieces
    # [+1][+2] or [+2][+1] or [-1][+2] or [-2][+1] or [-1][-2] or [-2][-1] or [+1][-2] or [+2][-1]
    
    def __init__(self):
        super().__init__()
        self.set_name("k")