from player import Player

class Human(Player):

    def __init__(self, player_name):
        self.player_type = 'human'
        super().__init__(player_name)