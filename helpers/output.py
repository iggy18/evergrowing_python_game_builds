from PROMPTS.text import GamePromt

class Display(GamePromt):
    
    def __init__(self):
        self.content = []
        
    def show(self):
        for line in self.content:
            print(line)
            
    def set_content(self, line):
        self.content.append(line)