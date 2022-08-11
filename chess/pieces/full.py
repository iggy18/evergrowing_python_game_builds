from .king import King
from .queen import Queen
from .pawn import Pawn
from .knight import Knight
from .rook import Rook
from .bishop import Bishop


def get_full_set(color):
    all_pieces = []
    for _ in range(8):
        pawn = Pawn()
        pawn.set_color(color)
        all_pieces.append(pawn)
        
    rook = Rook()
    rook.set_color(color)
    all_pieces.append(rook)
    
    knight = Knight()
    knight.set_color(color)
    all_pieces.append(knight)
    
    bishop = Bishop()
    bishop.set_color(color)
    all_pieces.append(bishop)
    
    queen = Queen()
    queen.set_color(color)
    all_pieces.append(queen)
    
    king = King()
    king.set_color(color)
    all_pieces.append(king)
    
    bishop = Bishop()
    bishop.set_color(color)
    all_pieces.append(bishop)
    
    knight = Knight()
    knight.set_color(color)
    all_pieces.append(knight)
    
    rook = Rook()
    rook.set_color(color)
    all_pieces.append(rook)
    
    return all_pieces

def get_both_chess_sets():
    white_pieces = get_full_set("W")
    black_pieces = get_full_set("B")
    return {'white' : white_pieces, 'black' : black_pieces}