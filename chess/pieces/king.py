from .piece import Piece

class King(Piece):
    
    #can move one square in any direction
    
    def __init__(self):
        super().__init__()
        self.set_name("K")