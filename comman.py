import random

class Camman:
    def __init__(self) -> None:
        self.ball_position = random.randint(1,3)

    def check_choise(self , choise):
        return choise == self.ball_position