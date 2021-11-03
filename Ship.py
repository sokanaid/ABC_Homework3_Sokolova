import random
from enum import Enum

import Transport


class ShipType(Enum):
    LINER = 1
    TUG_SHIP = 2
    TANKER = 3


class Ship(Transport):

    def __init__(self, *args):
        self.displacement = int(args[0])
        self.type = ShipType(int(args[1]))
        super().__init__(args[2::])

    def __init__(self):
        super().__init__()
        self.displacement = random.randint(10, 50000)
        self.type = ShipType(random.randint(1, 3))

    # Вывод
    def out(self, file):
        file.write("It is a ship: displacement = {}, type = {}".format(self.displacement, self.type))
        super().out(file)
