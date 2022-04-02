from abc import ABC, abstractmethod


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.point1 = Point(x1, y1)
        self.point2 = Point(x2, y2)

    def length(self):
        return round((abs(self.point1.x-self.point2.x)**2 + abs(self.point1.y-self.point2.y)**2)**0.5, 2)


class Shape(ABC):
    @abstractmethod
    def area():
        pass

    @abstractmethod
    def perimeter():
        pass


class Square(Line, Shape):
    def area(self):
        return round(((Line.length(self)**2)/2), 2)

    def perimeter(self):
        return round((Line.length(self)*(2**0.5)*2), 2)


class Rect(Shape):
    def __init__(self, x1, y1, x2, y2):
        self.width = Line(x1, y1, x2, y1).length()
        self.leng = Line(x1, y1, x1, y2).length()

    def area(self):
        return round((self.width * self.leng), 2)

    def perimeter(self):
        return round(2 * (self.leng + self.width), 2)


class Cube(Square):
    def volume(self):
        return round(Square.area(self)**(3/2), 2)


#a = Line(2, 5, 4, 8)
kvadrat = Square(1, 1, 3, 3) 
print(kvadrat.perimeter(), kvadrat.area(), kvadrat.length())


rectangl = Rect(1, 1, 3, 4)
print(rectangl.area(), rectangl.perimeter())

kubik = Cube(1, 1, 3, 3)
print(kubik.volume())
