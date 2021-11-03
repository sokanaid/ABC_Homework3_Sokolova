import Transport


class Container:
    def __int__(self):
        self.arr = []

    # Ввод данных
    def file_in(self, file):
        while True:
            try:
                self.arr.append(Transport.file_in())
            except:
                break

    # Заполнение рандомными данными
    def rnd_in(self, size):
        while len(self.arr) != size:
            transport = Transport.rnd_in()
            if transport != None:
                self.arr.append(transport)

    # Вывод данных
    def out(self, file):
        file.writeln("Container contains {} elements.".format(len(self.arr)))
        for i in range(len(self.arr)):
            file.write("{} :".format(i))
            self.arr[i].out(file)

    # Сортировка Шелла
    def shell_sort(self):
        first = 0
        last = len(self.arr);
        d = (last - first) // 2
        while d != 0:
            for i in range(first + d, last):
                j = i
                while j - first >= d and self.arr[j].ideal_time() < self.arr[(j - d)].ideal_time():
                    self.arr[j], self.arr[(j - d)] = self.arr[(j - d)], self.arr[j]
                    j -= d

            d //= 2
        return "Container was sorted."
