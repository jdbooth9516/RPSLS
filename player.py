class Player:
    def __init__(self):
        self.name = ''
        self.rounds_won = 0

class Human(Player):
    def __init__(self):
        super().__init__(self)

    def set_name(self):
        name = input("Choose your name: ")

        self. name = name



class Computer(Player):
    def __init__(self):
        super().__init__(self)

        self.name = "AI"

    def choose_gesture(self):
        pass