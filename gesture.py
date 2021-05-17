

class Rock:
    def __init__(self):
        self.name = 'rock'
        self.loses_to = ['paper', "spock"]


class Scissor:
    def __init__(self):
        self.name = 'scissor'
        self.loses_to = ['rock', "spock"]


class Paper:
    def __init__(self):
        self.name = 'paper'
        self.loses_to = ['scissor', "lizard"]


class Lizard:
    def __init__(self):
        self.name = 'lizard'
        self.loses_to = ['scissor', "rock"]


class Spock:
    def __init__(self):
        self.name = 'spock'
        self.loses_to = ['lizard', "paper"]