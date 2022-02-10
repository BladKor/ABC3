from random import randint

from enum import Enum

from transport import Transport


class ShipKind(Enum):
    LINER = "liner"
    TUG = "tug"
    TANKER = "tanker"


class Ship(Transport):
    def __init__(self):
        super().__init__()
        self.kind = None
        self.displacement = None

    def in_from_file(self, file):
        super(Ship, self).in_from_file(file)
        self.displacement = int(file.pop())
        ship_kind = str(file.pop())
        if ship_kind == "liner":
            self.kind = ShipKind.LINER
        elif ship_kind == "tug":
            self.kind = ShipKind.TUG
        elif ship_kind == "tanker":
            self.kind = ShipKind.TANKER
        else:
            raise RuntimeError("incorrect ship kind")

    def in_rnd(self):
        ship_kind = randint(1, 3)
        if ship_kind == 1:
            self.kind = ShipKind.LINER
        elif ship_kind == 2:
            self.kind = ShipKind.TUG
        elif ship_kind == 3:
            self.kind = ShipKind.TANKER
        super(Ship, self).in_rnd()
        self.displacement = randint(1, 100)

    def out(self, file):
        kind_str = "None"
        if self.kind == ShipKind.LINER:
            kind_str = "liner"
        elif self.kind == ShipKind.TUG:
            kind_str = "tug"
        elif self.kind == ShipKind.TANKER:
            kind_str = "tanker"

        file.write('Ship ' + kind_str + F' distance = {self.distance}, speed = {self.speed}, displacement = '
                                        F'{self.displacement}, optimal time = {self.optimal_time()}\n')
