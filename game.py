from human import Human
from bot import Bot
from player import Player



class Game:

    def __init__(self, player_count):
        self.player_count = player_count

        print("Game initializing...")

        if player_count == '0':
            # Create the two bots to battle eachother
            player1 = Bot()
            
            player2 = Bot()
            
        elif player_count == "1":
            # Create a Human based on the username inputted
            player1_name = input("Please input your username. ")
            player1 = Human('Charles')
            print(f"Player 1 created... Welcome {player1.player_name}!")
            
            # Create a bot
            player2 = Bot()

            
        elif player_count == "2":
            # Create a Human based on the username inputted
            player1_name = input("Please input your username. ")
            player1 = Human(player1_name)
            print(f"Player 1 created... Welcome {player1.player_name}!")
            
            # Create a Human based on the username inputted
            player2_name = input("Please input your username. ")
            player2 = Human(player2_name)
            print(f"Player 2 created... Welcome {player2.player_name}!")


    #def create_human_object(player_name):
    #    Human(Player(player_name))
    
        # if self.player_count == 1:
        #     player1_name = input("What is your name? ")
            
        #     player1 = Human(Player(player1_name))
        #     print(f"Welcome {player1.player_name}!")
        # elif self.player_count == 2:

    #def create_bot_object(self):
        

    