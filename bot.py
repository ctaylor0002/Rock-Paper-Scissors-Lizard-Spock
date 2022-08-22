from player import Player

class Bot(Player):
    
    def __init__(self, player_name):
        super().__init__(player_name)
        print("Bot Created!")
