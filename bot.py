from player import Player
import random

class Bot(Player):
    
    def __init__(self):
        self.player_type = 'bot'
        random_names = ["Roberto", "Gregory", "Robin", "Timmy", 'Ricardo', 'Judy']
        name_index = random.randrange(0,5)
        player_name = random_names[name_index]
        
        super().__init__(player_name)
        print("Bot Created!")
