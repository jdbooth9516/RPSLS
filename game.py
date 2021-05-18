from gesture import *
from player import *
import time
import random
import getpass


class Game:
    def __init__(self):
        self.rounds = 0
        self.current_round = 0
        self.players = 0
        self.player_1 = None
        self.player_2 = None
        self.run = False
        self.rock = Rock()
        self.paper = Paper()
        self.scissor = Scissor()
        self.lizard = Lizard()
        self.spock = Spock()
        self.gestures = [self.rock, self.paper, self.scissor, self.lizard, self.spock]
        self.round_winner = ""




    def run_game(self):
        self.main_menu()
        self.run = True
        while self.run == True:
            self.round_winner = self.decide_round()
            self.get_round_winner()
            self.determine_winner()


    def main_menu(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print()
        time.sleep(1)
        print('You must run this from the terminal by "cd" in to the directory and using the command "python3 main.py"')
        print()
        time.sleep(2)
        print("Rules are simply just like Rock, Paper, Scissors. Just with the addition of 2 more options of lizard and spock.")
        time.sleep(2)
        print()
        print('For the number of players enter 1 to play against the AI, enter 2 to play against another human')
        time.sleep(2)
        print()
        print('when choosing a gesture hit a single number and hit enter the number that you have selected will not '
              'be displayed in terminal.')
        print()
        valid_1 = False
        number_of_rounds = 0
        num_players = 0
        while valid_1 == False:
            num_players = int(input("Please select a number of players: (1 or 2): "))
            if num_players != 1 and num_players != 2:
                print("Invalid input please try again.")
            else:
                valid_1 = True

        valid_2 = False
        while valid_2 == False:
            number_of_rounds = int(input("Please select the best out of '' : for game length: "))
            if number_of_rounds % 2 == 0:
                print("Needs to be an odd number for best out of.")
            else:
                valid_2 = True

        self.rounds = number_of_rounds
        if num_players == 1:
            self.player_1 = Human()
            print("Player 1:")
            self.player_1.set_name()
            self.player_2 = Computer()

        else:
            self.player_1 = Human()
            print("player 1: ")
            self.player_1.set_name()
            self.player_2 = Human()
            print("player 2: ")
            self.player_2.set_name()

    def choose_gesture_player_1(self):
        print("Player 2 look away")
        print()
        time.sleep(2)
        player_1_choice = ""
        valid = False
        while valid == False:
            # player_1_choice = int(input("Choose a gesture by picking a number (1: rock) (2: paper) (3: scissors) (4: lizard) (5: Spock): ")) - 1
            player_1_choice = int(getpass.getpass("Choose a gesture by picking a number (1: rock) (2: paper) (3: scissors) (4: lizard) (5: Spock): ")) - 1
            if player_1_choice != 0 and player_1_choice != 1 and player_1_choice != 2 and player_1_choice != 3 and player_1_choice != 4:
                print("Invalid input please try again!")
            else:
                valid = True
        time.sleep(2)
        selected_gesture = self.gestures[player_1_choice]
        return selected_gesture

    def choose_gesture_player_2(self):
        if self.player_2.name == 'AI':
            player_2_choice = random.randint(0, 4)
            selected_gesture = self.gestures[player_2_choice]
            return selected_gesture
        else:
            print("Player 1 look away")
            print()
            time.sleep(2)
            player_2_choice = ""
            valid = False
            while valid == False:
                # player_2_choice = int(input(
                #     "Choose a gesture by picking a number (1: rock) (2: paper) (3: scissors) (4: lizard) (5: Spock): ")) - 1
                player_2_choice = int(getpass.getpass(
                    "Choose a gesture by picking a number (1: rock) (2: paper) (3: scissors) (4: lizard) (5: Spock): ")) - 1
                if player_2_choice != 0 and player_2_choice != 1 and player_2_choice != 2 and player_2_choice != 3 and player_2_choice != 4:
                    print("Invalid input please try again!")
                else:
                    valid = True
            time.sleep(2)
            selected_gesture = self.gestures[player_2_choice]
            return selected_gesture

    def decide_round(self):
        player_1_hand = self.choose_gesture_player_1()
        player_2_hand = self.choose_gesture_player_2()
        for lose in player_1_hand.loses_to:
            if lose == player_2_hand.name:
                result = 'player_2'
                print(f'{self.player_1.name} picked {player_1_hand.name} ')
                print()
                time.sleep(2)
                print(f'{self.player_2.name} picked {player_2_hand.name}')
                print()
                time.sleep(2)
                print(f'{result} won the round')
                print()
                self.current_round += 1
                return result

        for lose in player_2_hand.loses_to:
            if lose == player_1_hand.name:
                result = 'player_1'
                print(f'{self.player_1.name} picked {player_1_hand.name} ')
                print()
                time.sleep(1.5)
                print(f'{self.player_2.name} picked {player_2_hand.name}')
                print()
                time.sleep(1.5)
                print(f'{result} won the round')
                time.sleep(1.5)
                print()
                self.current_round += 1
                return result

        if player_1_hand.name == player_2_hand.name:
            result = "tie"
            print(f'{self.player_1.name} picked {player_1_hand.name} ')
            print()
            time.sleep(1.5)

            print(f'{self.player_2.name} picked {player_2_hand.name}')
            print()
            time.sleep(1.5)

            print('Round is tied')
            print()
            time.sleep(1.5)
            self.current_round += 1
            return result

    def get_round_winner(self):
        if self.round_winner == "player_1":
            self.player_1.rounds_won += 1
            print(f'Player One : {self.player_1.rounds_won} to Player Two : {self.player_2.rounds_won}')
            print()
            time.sleep(2)
        elif self.round_winner == "player_2":
            self.player_2.rounds_won += 1
            print(f'Player One : {self.player_1.rounds_won} to Player Two : {self.player_2.rounds_won}')
            print()
            time.sleep(2)

    def determine_winner(self):
        if self.player_1.rounds_won == (self.rounds // 2) + 1:
            print(f"{self.player_1.name} has WON the game!!!")
            self.play_again()

        if self.player_2.rounds_won == (self.rounds // 2) + 1:
            print(f"{self.player_2.name} has WON the game!!!")
            self.play_again()

        if self.current_round == self.rounds:
            if self.player_1.rounds_won > self.player_2.rounds_won:
                print(f"{self.player_1.name} has WON the game!!!")
                self.play_again()
            elif self.player_2.rounds_won > self.player_1.rounds_won:
                print(f'{self.player_2.name} has WON the game!!!')
                self.play_again()
            else:
                print("All right, we'll call it a draw")
                self.play_again()


    def play_again(self):
        selection = input("Do you want to play again? (y/n): ")
        valid_selection = selection.lower()
        if valid_selection == "y":
            self.player_1.rounds_won = 0
            self.player_2.rounds_won = 0
        else:
            self.run = False

