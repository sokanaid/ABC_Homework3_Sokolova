import Transport
import random


class Train(Transport):

    def __init__(self, *args):
        self.numberOfRailwayCarriage = int(args[0])
        super().__init__(args[1::])

    def __int__(self):
        super().__init__()
        self.numberOfRailwayCarriage = random.randint(1, 20)

    # Вывод
    def out(self, file):
        file.write("It is a train: number of railway carriage = {}".format(self.numberOfRailwayCarriage))
        super().out(file)
