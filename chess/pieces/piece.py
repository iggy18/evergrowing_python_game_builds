from colorama import init, Fore, Style
init(autoreset=True)

class Piece:
    
    def __init__(self):
        self.name = None
        self.color = None
        
    def __str__(self):
        return '{}'.format(Fore.GREEN + self.name if self.color == "W" else Fore.RED + self.name) + Style.RESET_ALL

    
    def __repr__(self):
        return '{}'.format(Fore.GREEN + self.name if self.color == "W" else Fore.RED + self.name) + Style.RESET_ALL
    
    def set_color(self, color):
        self.color = color
    
    def set_name(self, name):
        self.name = name