import math


class Transport(object):
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + " и " + other.name


class Square(object):
    def __init__(self, w):
        self.w = w

    def __add__(self, other):
        return math.sqrt(self.w ** 2 + other.w ** 2)


def example1():
    t1 = Transport("автомобиль")
    t2 = Transport("мотоцикл")
    sq1 = Square(2)
    sq2 = Square(1)

    return ("Применим оператор сложения к 2м экземпляром класса Square, в результате получим: " + str(sq1 + sq2) +
            "\nПрименим оператор сложения к 2м экземпляром класса Transport, в результате получим: " + (t1 + t2) +
            "\nЭто происходит по причине того, что мы заранее определили поведение объектов классов при их сложенеии"
            "\nЭто является одним из примеров полиморфизма")
