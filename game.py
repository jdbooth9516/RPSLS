from gesture import *
from player import *

class Game:
    def __init__(self):
        self.rounds = 3
        self.players = 0
        self.player_1 = None
        self.player_2 = None
        self.run = False



    def run_game(self):
        self.main_menu()

    def main_menu(self):
        num_players = int(input("Please select a number of players: (1 or 2): "))
        number_of_rounds = int(input("Please select the best out of '' : for game length "))

        if num_players == 1:
            self.player_1 = Human()
            self.player_1.set_name()
            self.player_2 = Computer()

        else:
            self.player_1 = Human()
            self.player_1.set_name()
            self.player_2 = Human()
            self.player_2.set_name()


    def round(self):
        pass


    def choose_gesture(self):
        pass

    def decide_round(self):
        pass

    def determine_winner(self):
        pass



