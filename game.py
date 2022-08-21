from human import Human
from bot import Bot
from player import Player
import random


class Game:

    def __init__(self, player_count):
        self.player_count = player_count

        if player_count == '0':
            print("Game initializing...")
            the_game = Game(player_count)

            # Create the two bots to battle eachother
            self.player1 = the_game.create_bot_object()
            print(f"Player 1 created... Welcome {self.player1.player_name}!")
            
            self.player2 = the_game.create_bot_object()
            print(f"Player 2 created... Welcome {self.player2.player_name}!")

        elif player_count == "1":
            print("Game initializing...")
            the_game = Game(player_count)

            # Create a Human based on the username inputted
            player1_name = input("Please input your username. ")
            self.player1 = the_game.create_human_object(player1_name)
            print(f"Player 1 created... Welcome {self.player1.player_name}!")
            
            # Create a bot
            self.player2 = the_game.create_bot_object()
            print(f"Player 2 created... Welcome {self.player2.player_name}!")

        elif player_count == "2":
            print("Game initializing...")
            the_game = Game(player_count)

            player1_name = input("Please input your username. ")
            self.player1 = the_game.create_human_object(player1_name)
            print(f"Player 1 created... Welcome {self.player1.player_name}!")
            
            player2_name = input("Please input your username. ")
            self.player2 = the_game.create_human_object(player2_name)
            print(f"Player 2 created... Welcome {self.player2.player_name}!")


    def create_human_object(self, player_name):
        Human(Player(player_name))
    
        # if self.player_count == 1:
        #     player1_name = input("What is your name? ")
            
        #     player1 = Human(Player(player1_name))
        #     print(f"Welcome {player1.player_name}!")
        # elif self.player_count == 2:

    def create_bot_object(self):
        random_names = ["Roberto", "Gregory", "Robin", "Timmy", 'Ricardo', 'Judy']
        name_index = random.randrange(0,5)
        Bot(Player(random_names[name_index]))

    