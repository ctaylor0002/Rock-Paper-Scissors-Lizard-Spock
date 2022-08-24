from human import Human
from bot import Bot
from player import Player
from time import sleep
import random



class Game:

    def __init__(self):
        self.player1 = ""
        self.player2 = ""

        self.init_players()

    def display_rules(self):
        rule_list = ["Rock crushes Scissors", "Scissors cuts Paper", "Paper covers Rock", "Rock crushes Lizard", "Lizard poisons Spock", "Spock smashes Scissors", "Scissors decapitates Lizard", "Lizard eats Paper", "Paper disproves Spock", "Spock vaporizes Rock"]
        print(f'\nContestant 1, {self.player1.player_name} will be facing off against contestant 2, {self.player2.player_name} in a best of 3 battle of Rock Paper Scissors Lizard Spock!')
        sleep(1)
        print('\nHere are the rules...')
        sleep(1)

        for rule in rule_list:
            print(f'{rule}')
            sleep(1)

        print('\n')

    def init_players(self):
        valid_input = False
        while valid_input == False:
            player_count = input("How many players will be participating? (0-2) ")
            
            if player_count == '0' or player_count == '1' or player_count == '2':
                self.player_count = player_count
                print("Game initializing...")

            if player_count == '0':
                # Create the two bots to battle eachother
                self.player1 = Bot()
                
                self.player2 = Bot()
                
                valid_input = True

            elif player_count == "1":
                # Create a Human based on the username inputted
                player1_name = input("Please input your username. ")
                self.player1 = Human(player1_name)
                print(f"Player 1 created... Welcome {self.player1.player_name}!")
                
                # Create a bot
                self.player2 = Bot()

                valid_input = True
            
            elif player_count == "2":
                # Create a Human based on the username inputted
                player1_name = input("Please input your username. ")
                self.player1 = Human(player1_name)
                print(f"Player 1 created... Welcome {self.player1.player_name}!")
                
                # Create a Human based on the username inputted
                player2_name = input("Please input your username. ")
                self.player2 = Human(player2_name)
                print(f"Player 2 created... Welcome {self.player2.player_name}!")

                valid_input = True
            else:
                print("Invalid player count. Please try again.")

        self.display_rules()
        

    def run_round_human(self, player):
        # Run player 1 pick
        picked_action = False
        while picked_action == False:
            player_picked_action = input(f"{player.player_name}, please pick an action. (Rock, Paper, Scissors, Lizard, Spock) ")
            for action in player.action_list:
                if player_picked_action.title() == action:
                    picked_action = True
                    player.current_action = player_picked_action.title()
                    break
            if player.current_action == "":
                print("Invalid action. Please try again...")
        
        

    def run_round_bot(self, player):
        action = player.action_list[random.randrange(0,4)]
        player.current_action = action
        sleep(1)
        print(f"{player.player_name} has picked an action!")

    def run_round(self):
        
        if self.player1.player_type == 'human':
            self.run_round_human(self.player1)
        else:
            self.run_round_bot(self.player1)

        if self.player2.player_type == 'human':
            self.run_round_human(self.player2)
        else:
            self.run_round_bot(self.player2)

        print('\nRock!')
        sleep(1)
        print('Paper!')
        sleep(1)
        print('Scissors!')
        sleep(1)
        print('Lizard!')
        sleep(1)
        print('Spock!')
        sleep(1)
        print('Shoot!\n')
        sleep(1)

        print(f"{self.player1.player_name} has picked... {self.player1.current_action}")
        sleep(1)
        print(f"{self.player2.player_name} has picked... {self.player2.current_action}")
        sleep(1)

    def run_game(self):
        # Hard code the victories until I can think of a better method
        finished_game = False

        while finished_game == False:
            
            self.run_round()

            player1_action = self.player1.current_action
            player2_action = self.player2.current_action
            if self.player1.current_action == self.player2.current_action:
                print('Its a tie!')
                continue
        
            if player1_action == "Rock":
                if player2_action == "Paper" or player2_action == "Spock":
                    print(f"{self.player2.player_name} wins this round!")
                    self.player2.rounds_won += 1
                elif player2_action == "Scissors" or player2_action == "Lizard":
                    print(f"{self.player1.player_name} wins this round!")
                    self.player1.rounds_won += 1
            elif player1_action == "Paper":
                if player2_action == "Scissors" or player2_action == "Lizard":
                    print(f"{self.player2.player_name} wins this round!")
                    self.player2.rounds_won += 1
                elif player2_action == "Rock" or player2_action == "Spock":
                    print(f"{self.player1.player_name} wins this round!")
                    self.player1.rounds_won += 1
            elif player1_action == "Scissors":
                if player2_action == "Rodck" or player2_action == "Spock":
                    print(f"{self.player2.player_name} wins this round!")
                    self.player2.rounds_won += 1
                elif player2_action == "Paper" or player2_action == "Lizard":
                    print(f"{self.player1.player_name} wins this round!")
                    self.player1.rounds_won += 1
            elif player1_action == "Lizard":
                if player2_action == "Rock" or player2_action == "Scissors":
                    print(f"{self.player2.player_name} wins this round!")
                    self.player2.rounds_won += 1
                elif player2_action == "Paper" or player2_action == "Spock":
                    print(f"{self.player1.player_name} wins this round!")
                    self.player1.rounds_won += 1
            elif player1_action == "Spock":
                if player2_action == "Lizard" or player2_action == "Paper":
                    print(f"{self.player2.player_name} wins this round!")
                    self.player2.rounds_won += 1
                elif player2_action == "Scissors" or player2_action == "Rock":
                    print(f"{self.player1.player_name} wins this round!")
                    self.player1.rounds_won += 1
            sleep(1)
            if self.player1.rounds_won == 2:
                print(f"\n{self.player1.player_name} has won the best of 3!")
                finished_game = True
            elif self.player2.rounds_won == 2:
                print(f"\n{self.player2.player_name} has won the best of 3!")
                finished_game = True
                #play_again = False

                #while play_again == False
                #    play_again_coice = input("Would you like to play again? y/n")
                #    if play_again_coice == 'y':




    #def create_human_object(player_name):
    #    Human(Player(player_name))
    
        # if self.player_count == 1:
        #     player1_name = input("What is your name? ")
            
        #     player1 = Human(Player(player1_name))
        #     print(f"Welcome {player1.player_name}!")
        # elif self.player_count == 2:

    #def create_bot_object(self):
        

    