from .piece import Piece

class Pawn(Piece):
    
    #can move away from its starting position
    #can move diagonally only when attacking
    #can move two squares only on its first move
    #can only attack diagonally
    #be promoted when reaching the other side of the board
    #can be promoted to a queen, rook, bishop, or knight
    #can not jump over other pieces
    
    def __init__(self):
        super().__init__()
        self.set_name("P")