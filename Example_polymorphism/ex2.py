class Figure(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def s(self):
        pass


class Square(Figure):

    def __init__(self, x=0, y=0, a=0):
        super().__init__(x, y)
        self.a = a

    def s(self):
        return self.a ** 2


class Rectangle(Figure):

    def __init__(self, x=0, y=0, a=0, b=0):
        super().__init__(x, y)
        self.a = a
        self.b = b

    def s(self):
        return self.a * self.b


def example2():
    a = Square(0, 0, 20)
    b = Rectangle(0, 0, 20, 30)
    return "Площадь квадрата = " + str(a.s()) + "\nПлощадь прямоугольника = " + str(b.s())
