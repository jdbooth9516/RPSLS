class Gesture:
    def __init__(self):
        self.name = ''
        self.wins_against = []
        self.loses_to = []


class Rock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'rock'
        self.wins_against = ['scissors', "lizard"]
        self.loses_to = ['paper', "spock"]


class Scissor(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'scissor'
        self.wins_against = ['paper', "lizard"]
        self.loses_to = ['rock', "spock"]


class Paper(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'paper'
        self.wins_against = ['rock', "spock"]
        self.loses_to = ['scissor', "lizard"]


class Lizard(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'lizard'
        self.wins_against = ['spock', "paper"]
        self.loses_to = ['scissor', "rock"]


class Spock(Gesture):
    def __init__(self):
        super().__init__()
        self.name = 'spock'
        self.wins_against = ['scissors', "rock"]
        self.loses_to = ['lizard', "paper"]