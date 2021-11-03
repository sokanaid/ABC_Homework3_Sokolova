import Train
import Plane
import Ship
import random


class Transport:
    def __init__(self, *args):
        self.speed = int(args[0])
        self.distance = float(args[1])

    def __int__(self):
        self.speed = random.randint(1, 500)
        self.distance = random.uniform(1, 10000)

    # Ввод транспорта из файла
    @staticmethod
    def file_in(file):
        k, args = file.readline().split()
        k = int(k)
        if k == 1:
            sp = Train(args)
        elif k == 2:
            sp = Ship(args)
        elif k == 3:
            sp = Plane(args)
        return sp

    # Ввод рандомного транспорта
    @staticmethod
    def rnd_in(file):
        k = random.randint(1, 3)
        k = int(k)
        if k == 1:
            sp = Train()
        elif k == 2:
            sp = Ship()
        elif k == 3:
            sp = Plane()
        return sp

    # Идельное время
    def ideal_time(self) -> float:
        return self.distance / self.speed

    # Вывод общих характеристик
    def out(self, file):
        file.write(
            ", speed = {}, distance = {}. Ideal time = {}\n".format(self.speed, self.distance, self.ideal_time()))
