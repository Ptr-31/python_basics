# Создайте класс Shape (геометрическая фигура) со свойствами name и color (название и цвет). У этого класса должны быть три
# подкласса – Circle (окружность), Rectangle (прямоугольник), и Triangle (треугольник). Каждый подкласс наследует атрибут color и
# методdescribe() родительского класса Shape, и при этом имеет дополнительные свойства и методы:
#
# Circle – атрибут radius и метод area() для вычисления площади.
# Rectangle – атрибуты length и width, свой метод area().
# Triangle – атрибуты base и height (основание и высота), собственный метод area().

import math


class Shape:
    def __init__(self, color):
        self.color = color

    def describe(self):
        print(f'Это геометрическая фигура, цвет - {self.color}')


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return round(math.pi * self.radius * self.radius, 2)

    def describe(self):
        super(Circle, self).describe()
        print(f'Это окружность, радиусом {self.radius}cm, цвет - {self.color}')


class Rectangle(Shape):
    def __init__(self, color, side_a, side_b):
        super(Rectangle, self).__init__(color)
        self.side_a = side_a
        self.side_b = side_b

    def area(self):
        return self.side_a * self.side_b

    def describe(self):
        super().describe()
        print(f'Это прямоугольник. Длина - {self.side_a}, ширина - {self.side_b}. Цвет - {self.color} ')

class Triangle(Shape):
    def __init__(self, color, base, hight):
        super(Triangle, self).__init__(color)
        self.base = base
        self.hight = hight

    def area(self):
        return self.base/2 * self.hight

    def describe(self):
        super(Triangle, self).describe()
        print(f'Это {self.color} треугольник с основанием {self.base} см и высотой {self.hight} см')

def main():
    circle = Circle("красный", 5)
    circle.describe()
    rectangle = Rectangle("синий", 3, 4)
    triangle = Triangle("фиолетовый", 6, 8)
    rectangle.describe()
    triangle.describe()
    print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см^2.")


if __name__ == '__main__':
    main()
