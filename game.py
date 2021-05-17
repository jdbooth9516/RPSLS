from gesture import *


class Game:
    def __init__(self):
        self.rounds = 3
        self.players = 0


    def main_menu(self):
        num_players = int(input("Please select a number of players: (1 or 2): "))
        number_of_rounds = int(input("Please select the best out of '' : for game length "))


