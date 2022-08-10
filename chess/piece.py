class Piece:
    
    def __init__(self):
        self.name = None
        self.color = None
        self.current_position = None
        self.possible_moves = []
        
    def __str__(self):
        return self.color + " " +self.name + " " + self.current_position
    
    def get_possible_moves(self, board):
        pass
    
    def move(self, new_position):
        pass