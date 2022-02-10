from random import randint

from transport import Transport


class Airplane(Transport):
    def __init__(self):
        super().__init__()
        self.fly_distance = None
        self.load_capacity = None

    def in_from_file(self, file):
        super(Airplane, self).in_from_file(file)
        self.fly_distance = int(file.pop())
        self.load_capacity = int(file.pop())

    def in_rnd(self):
        super(Airplane, self).in_rnd()
        self.fly_distance = randint(1, 100)
        self.load_capacity = randint(1, 100)

    def out(self, file):
        file.write(F'Airplane distance = {self.distance}, speed = {self.speed}, fly distance = {self.fly_distance}, '
                   F'load capacity = {self.load_capacity} optimal time = {self.optimal_time()}\n')

    def optimal_time(self):
        return self.fly_distance / self.speed
