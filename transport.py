import random


class Transport:
    def __init__(self, *args):
        if len(args):
            self.speed = int(args[0])
            self.distance = float(args[1])
        else:
            self.speed = random.randint(1, 500)
            self.distance = random.uniform(1, 10000)

            # Идельное время

    def ideal_time(self) -> float:
        return self.distance / self.speed

    # Вывод общих характеристик
    def out(self, file):
        file.write(
            ", speed = {}, distance = {}. Ideal time = {:.5f}\n".format(self.speed, self.distance, self.ideal_time()))
