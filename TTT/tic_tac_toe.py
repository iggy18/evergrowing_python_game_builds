from helpers.input import *
from helpers.output import Display

class TicTacToe:
    
    def __init__(self):
        self.current_player = "X"
        self.board = {
            "1" : " ",
            "2" : " ",
            "3" : " ",
            "4" : " ",
            "5" : " ",
            "6" : " ",
            "7" : " ",
            "8" : " ",
            "9" : " "
        }
        self.winners = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            [1,4,7],
            [2,5,8],
            [3,6,9],
            [1,5,9],
            [3,5,7]
        ]
        self.display = Display()
    
    def check_for_win(self, a, b, c):
        if self.board[a] != ' ':
            return self.board[a] == self.board[b] == self.board[c]

    def scan_board(self):
        for box in self.winners:
            if self.check_for_win(str(box[0]), str(box[1]), str(box[2])):
                self.reset()
                print("{}  has won!".format(self.current_player))

    def reset(self):
        for key, value in self.board.items():
            if value != ' ':
                self.board[key] = ' '
    
    def turn(self):
        if self.current_player == "X":
            self.current_player = "Y"
            return
        if self.current_player == "Y":
            self.current_player = "X"
            return
    
    def empty(self, position):
        return self.board[position] != ' '

    def try_again(self):
        print("that spot is taken")
        
    def place(self, position):
        if not self.empty(position):
            self.board[position] = self.current_player
            self.scan_board()
            self.turn()
        else:
            self.try_again()
    
    def square(self, num):
        return self.board[str(num)]
    
    def load_board(self):
        line = 1
        while line != 10:
            text = "\n{} | {} | {}".format(self.square(line), self.square(line +1), self.square(line +2))
            border = "---------"
            if line <= 7:
                self.display.set_content(border)
            self.display.set_content(text)
            line += 3

    def play(self):
        while True:
            self.load_board()
            self.display.show()
            chose = input('place your token.\n>>> ')
            self.place(chose)