import random

import transport


class Plane(transport.Transport):
    def __init__(self, *args):
        self.flightRange = int(args[0])
        self.liftingCapacity = int(args[1])
        super().__init__(args[2::])

    def __init__(self):
        super().__init__()
        self.flightRange = random.randint(10, 50000)
        self.liftingCapacity = random.randint(10, 50000)

    # Вывод
    def out(self, file):
        file.write(
            "It is a plane: flight range = {}, lifting capacity = {}".format(self.flightRange, self.liftingCapacity))
        super().out(file)
