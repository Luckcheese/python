import random
import time


class Atom:
    def __init__(self):
        self.status = 'x'

    def update(self, decay_rate):
        if self.status == 'x' and random.random() < decay_rate:
            self.status = '.'

    def decayed(self):
        return self.status == '.'


class Matrix:
    dots = []

    def __init__(self, width, height, decay_rate_percentage):
        if decay_rate_percentage > 1:
            raise ValueError("decay_rate_percentage must be a floating number between 0 and 1")

        self.width = width
        self.height = height
        self.decay_rate = decay_rate_percentage

        self.dots = []
        self.create_dots()

    def create_dots(self):
        def create_row():
            return [Atom() for i in range(self.width)]

        self.dots = [create_row() for i in range(self.height)]

    def update(self):
        def update_row(i):
            [atom.update(self.decay_rate) for atom in self.dots[i]]

        [update_row(i) for i in range(self.height)]

    def __iter__(self):
        self.i = -1
        return self

    def next(self):
        self.i += 1

        row = self.i / self.width
        if row >= self.height:
            raise StopIteration()

        column = self.i % self.width
        return self.dots[row][column]

    def __str__(self):
        def print_row(i):
            return " ".join([atom.status for atom in self.dots[i]])

        return "\n".join([print_row(i) for i in range(self.height)])


class Report:
    all_counter = 0
    decayed_counter = 0
    decayed_percentage = 0.0
    cycle = -1

    def __init__(self, matriz):
        self.matrix = matriz
        self.all_counter = self.matrix.width * self.matrix.height
        self.update()

    def update(self):
        self.cycle += 1
        self.decayed_counter = 0

        for atom in self.matrix:
            if atom.status != 'x':
                self.decayed_counter += 1

        self.decayed_percentage = float(self.decayed_counter) / float(self.all_counter)

    def __str__(self):
        return """
        Cycle number: %d
        Total atoms: %d
        Decayed: %d (%f)
        """ % (self.cycle, self.all_counter, self.decayed_counter, self.decayed_percentage)


def update():
    m.update()
    r.update()


m = Matrix(5, 7, 0.3)
r = Report(m)

while r.decayed_percentage < 1:
    update()
    print m
    print r
    time.sleep(3)
