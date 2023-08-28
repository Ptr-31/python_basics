# Для ПО ресторана нужно разработать модуль, помогающий контролировать использование фруктов и овощей на кухне.
# Создайте абстрактный класс Ingredient с методами get_name() и get_quantity(). Затем создайте два подкласса Vegetable
# и Fruit, которые наследуют абстрактные методы от Ingredient и реализуют свои собственные версии методов get_name() и get_quantity().

from abc import ABC, abstractmethod

class Ingredient(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_quantity(self):
        pass

class Vegetable(Ingredient):
    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    def get_name(self):
        print(self.__name)

    def get_quantity(self):
        print(f'{self.__quantity} kg')

class Fruit(Ingredient):
    def __init__(self, name, quantity):
        self.__name = name
        self.__quantity = quantity

    def get_name(self):
        print(self.__name)

    def get_quantity(self):
        print(f'{self.__quantity} kg')


def main():
    carrot = Vegetable('Морковь', 5)
    carrot.get_name()
    carrot.get_quantity()

    apple = Fruit('Яблоко', 3)
    apple.get_name()
    apple.get_quantity()

if __name__ == '__main__':
    main()