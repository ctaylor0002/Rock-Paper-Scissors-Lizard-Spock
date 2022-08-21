from human import Human
# from bot import Bot
from player import Player


class Game:

    def __init__(self, player_count):
        self.player_count = player_count

    def create_player_objects(self):
        if self.player_count == 1:
            player1_name = input("What is your name? ")
            
            player1 = Human(Player(player1_name))
            print(f"Welcome {player1.player_name}!")
    