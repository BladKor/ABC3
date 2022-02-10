from random import randint

from airplane import Airplane
from ship import Ship
from train import Train


class Container:
    def __init__(self):
        self.data = []

    def in_from_file(self, file):
        while len(file) > 0:
            transport_kind = str(file.pop())
            transport = None
            if transport_kind == "airplane":
                transport = Airplane()
            elif transport_kind == "ship":
                transport = Ship()
            elif transport_kind == "train":
                transport = Train()
            else:
                raise RuntimeError(F"unexpected transport kind {transport_kind}")

            transport.in_from_file(file)
            self.data.append(transport)

    def in_rnd(self, n):
        for i in range(n):
            transport_kind = randint(1, 3)
            transport = None
            if transport_kind == 1:
                transport = Airplane()
            elif transport_kind == 2:
                transport = Ship()
            elif transport_kind == 3:
                transport = Train()

            transport.in_rnd()
            self.data.append(transport)

    def out(self, file):
        for i in range(len(self.data)):
            file.write(F'{i + 1}: ')
            self.data[i].out(file)

    def shaker_sort(self):
        swapped = True
        start = 0
        end = len(self.data) - 1
        while swapped:
            swapped = False
            for i in range(start, end):
                if self.data[i].optimal_time() < self.data[i + 1].optimal_time():
                    self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]
                    swapped = True
            if not swapped:
                break
            swapped = False
            end -= 1
            for i in range(end - 1, start - 1, -1):
                if self.data[i].optimal_time() < self.data[i + 1].optimal_time():
                    self.data[i], self.data[i + 1] = self.data[i + 1], self.data[i]
                    swapped = True
            start += 1
