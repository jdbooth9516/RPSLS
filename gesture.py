class Gesture:
    def __init__(self, name):
        self.name = name

class Rock(Gesture):
    def __init__(self):
        super().__init__(name='rock')
        self.loses_to = ['paper', "spock"]


class Scissor(Gesture):
    def __init__(self):
        super().__init__(name='scissor')
        self.loses_to = ['rock', "spock"]


class Paper(Gesture):
    def __init__(self):
        super().__init__(name='paper')
        self.loses_to = ['scissor', "lizard"]


class Lizard(Gesture):
    def __init__(self):
        super().__init__(name='lizard')
        self.loses_to = ['scissor', "rock"]


class Spock(Gesture):
    def __init__(self):
        super().__init__(name='spock')
        self.loses_to = ['lizard', "paper"]
