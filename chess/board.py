from colorama import init
init(autoreset=True)

from colorama import Fore, Back


class Board:
    
    def __init__(self):
        self.board = [[None for x in range(8)] for y in range(8)]
    
    def display(self):
        bottom = "   a b c d e f g h"
        boarder = "  -----------------"
        number = 1
        print(boarder)
        for row in self.board:
            print('{}| {} |'.format(number, ' '.join(str(x) if x is not None else str(0) for x in row)))
            number += 1
        print(boarder)
        print(bottom)