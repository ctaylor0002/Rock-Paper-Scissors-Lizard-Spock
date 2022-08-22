from human import Human
from bot import Bot
from player import Player
import random


class Game:

    def __init__(self, player_count):
        self.player_count = player_count

        print("Game initializing...")

        if player_count == '0':
            # Create the two bots to battle eachother
            self.player1 = Game.create_bot_object()
            
            self.player2 = Game.create_bot_object()
            
        elif player_count == "1":
            # Create a Human based on the username inputted
            player1_name = input("Please input your username. ")
            player1 = Game.create_human_object(self, player1_name)
            print(f"Player 1 created... Welcome {player1_name}!")
            
            # Create a bot
            self.player2 = Game.create_bot_object(self)
            
        elif player_count == "2":
            # Create a Human based on the username inputted
            player1_name = input("Please input your username. ")
            self.player1 = Game.create_human_object(self, player1_name)
            print(f"Player 1 created... Welcome {player1_name}!")
            
            # Create a Human based on the username inputted
            player2_name = input("Please input your username. ")
            self.player2 = Game.create_human_object(self, player2_name)
            print(f"Player 2 created... Welcome {player2_name}!")


    def create_human_object(self, player_name):
        Human(player_name)
    
        # if self.player_count == 1:
        #     player1_name = input("What is your name? ")
            
        #     player1 = Human(Player(player1_name))
        #     print(f"Welcome {player1.player_name}!")
        # elif self.player_count == 2:

    def create_bot_object(self):
        random_names = ["Roberto", "Gregory", "Robin", "Timmy", 'Ricardo', 'Judy']
        name_index = random.randrange(0,5)
        Bot(random_names[name_index])

    