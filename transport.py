from random import randint


class Transport:
    def __init__(self):
        self.distance = None
        self.speed = None

    def in_from_file(self, file):
        self.distance = int(file.pop())
        self.speed = int(file.pop())

    def in_rnd(self):
        self.distance = randint(1, 100)
        self.speed = randint(1, 100)

    def optimal_time(self):
        return self.distance / self.speed
