from human import Human
from bot import Bot
from player import Player
from time import sleep



class Game:

    def __init__(self):
        valid_input = False
        while valid_input == False:
            player_count = input("How many players will be participating? (0-2) ")

            if player_count == '0' or player_count == '1' or player_count == '2':
                self.player_count = player_count
                print("Game initializing...")

            if player_count == '0':
                # Create the two bots to battle eachother
                player1 = Bot()
                
                player2 = Bot()
                
                valid_input = True

            elif player_count == "1":
                # Create a Human based on the username inputted
                player1_name = input("Please input your username. ")
                player1 = Human(player1_name)
                print(f"Player 1 created... Welcome {player1.player_name}!")
                
                # Create a bot
                player2 = Bot()

                valid_input = True
            
            elif player_count == "2":
                # Create a Human based on the username inputted
                player1_name = input("Please input your username. ")
                player1 = Human(player1_name)
                print(f"Player 1 created... Welcome {player1.player_name}!")
                
                # Create a Human based on the username inputted
                player2_name = input("Please input your username. ")
                player2 = Human(player2_name)
                print(f"Player 2 created... Welcome {player2.player_name}!")

                valid_input = True
            else:
                print("Invalid player count. Please try again.")

        Game.display_rules(self, player1.player_name, player2.player_name)

    def display_rules(self, player1, player2):
        rule_list = ["Scissors cuts Paper", "Paper covers Rock", "Rock crushes Lizard", "Lizard poisons Spock", "Spock smashes Scissors", "Scissors decapitates Lizard", "Lizard eats Paper", "Paper disproves Spock", "Spock vaporizes Rock"]
        print(f'\nContestant 1, {player1} will be facing off against contestant 2, {player2} in a best of 3 battle of Rock Paper Scissors Lizard Spock!')
        sleep(1)
        print('\nHere are the rules...')
        
        for rule in rule_list:
            print(f'{rule}')
            sleep(1)


    #def create_human_object(player_name):
    #    Human(Player(player_name))
    
        # if self.player_count == 1:
        #     player1_name = input("What is your name? ")
            
        #     player1 = Human(Player(player1_name))
        #     print(f"Welcome {player1.player_name}!")
        # elif self.player_count == 2:

    #def create_bot_object(self):
        

    