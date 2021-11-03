import random

from plane import Plane
from ship import Ship
from train import Train
from transport import Transport


class Container:
    def __init__(self):
        self.arr = []

    # Ввод данных
    def file_in(self, file):
        while True:
            try:
                self.arr.append(Container.file_in_transport(file))
            except:
                break

    # Ввод транспорта из файла
    @staticmethod
    def file_in_transport(file):
        args = file.readline().split()
        k = int(args[0])
        if k == 1:
            sp = Train(args[1], args[2], args[3])
        elif k == 2:
            sp = Ship(args[1], args[2], args[3],args[4])
        elif k == 3:
            sp = Plane(args[1], args[2], args[3], args[4])
        return sp

    # Ввод рандомного транспорта

    @staticmethod
    def rnd_in_transport():
        k = random.randint(1, 3)
        k = int(k)
        if k == 1:
            sp = Train()
        elif k == 2:
            sp = Ship()
        elif k == 3:
            sp = Plane()
        return sp

    # Заполнение рандомными данными
    def rnd_in(self, size):
        while len(self.arr) != size:
            transport = Container.rnd_in_transport()
            if transport != None:
                self.arr.append(transport)

    # Вывод данных
    def out(self, file):
        file.write("Container contains {} elements.\n".format(len(self.arr)))
        for i in range(len(self.arr)):
            file.write("{}: ".format(i))
            self.arr[i].out(file)

    # Сортировка Шелла
    def shell_sort(self):
        first = 0
        last = len(self.arr)
        d = (last - first) // 2
        while d != 0:
            for i in range(first + d, last):
                j = i
                while j - first >= d and self.arr[j].ideal_time() < self.arr[(j - d)].ideal_time():
                    self.arr[j], self.arr[(j - d)] = self.arr[(j - d)], self.arr[j]
                    j -= d

            d //= 2
        return "Container was sorted.\n"
