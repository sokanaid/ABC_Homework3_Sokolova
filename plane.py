import random

import transport


class Plane(transport.Transport):

    def __init__(self, *args):
        if len(args):
            self.flight_range = int(args[0])
            self.lifting_capacity = int(args[1])
            super().__init__(args[2], args[3])
        else:
            super().__init__()
            self.flight_range = random.randint(10, 50000)
            self.lifting_capacity = random.randint(10, 50000)

    # Вывод
    def out(self, file):
        file.write(
            "It is a plane: flight range = {}, lifting capacity = {}".format(self.flight_range, self.lifting_capacity))
        super().out(file)
