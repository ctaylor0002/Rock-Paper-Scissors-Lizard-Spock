
class Player:

    def __init__(self, player_name):
        self.player_name = player_name
        self.rounds_won = 0
        self.current_action = ""
        self.action_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    