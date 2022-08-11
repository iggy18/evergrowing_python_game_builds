class ChessBoardSquare:
    
    def __init__(self):
        self.shade = None
        self.piece = None
        self.is_empty = True
        
    def set_piece(self, piece):
        self.piece = piece
        self.is_empty = False
        
    def remove_piece(self):
        self.piece = None
        self.is_empty = True
        
    def __str__(self):
        if self.is_empty:
            return "0"
        else:
            return self.piece.__str__()