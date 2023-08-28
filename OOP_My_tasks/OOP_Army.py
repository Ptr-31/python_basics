# Для военной стратегии необходимо создать абстрактный класс Soldier. Каждый солдат должен уметь двигаться, защищаться
# и атаковать, поэтому Soldier имеет три абстрактных метода: move(), attack() и defend(). Два конкретных класса,
# Infantry (пехота) и Cavalry (кавалерия), будут наследовать и реализовывать эти методы. В игре также должен быть класс
# Army, который будет добавлять солдат в армию и выполнять операции атаки и защиты.
#
# Чтобы гарантировать, что используются только экземпляры класса Soldier, нужно создать декоратор validatesoldier,
# который будет проверять тип объекта. Если объект не является экземпляром класса Soldier, декоратор выдаст ошибку TypeError.
# Декоратор будет применяться к методам move(), attack() и defend() классов Infantry и Cavalry.

from abc import ABC, abstractmethod

def validate_soldier(func):
    def wrapper(self):
        if not isinstance(self, Soldier):
            raise TypeError('Объект не является экземпляром класса Soldier!')
        return func(self)
    return wrapper

class Soldier(ABC):
    def move(self):
        pass

    def attack(self):
        pass

    def defend(self):
        pass

class Infantry(Soldier):
    @validate_soldier
    def move(self):
        print('Пехота передвигается в пешем порядке')

    @validate_soldier
    def attack(self):
        print('Пехота участвует в ближнем бою')

    @validate_soldier
    def defend(self):
        print('Пехота держит строй')

class Cavalry(Soldier):
    @validate_soldier
    def move(self):
        print('Кавалерия передвигается верхом')

    @validate_soldier
    def attack(self):
        print('Кавалерия переходит в атаку')

    @validate_soldier
    def defend(self):
        print('Кавалерия защищает фланги')

class Army:
    army = []

    def add_soldier(self, soldier):
        self.army.append(soldier)

    def attack(self):
        for soldier in self.army:
            soldier.move()
            soldier.attack()

    def defend(self):
        for soldier in self.army:
            soldier.move()
            soldier.defend()
class Check():
    @validate_soldier
    def move(self):
        print('Кавалерия передвигается верхом')
def main():
    army = Army()
    army.add_soldier(Check)
    # army.add_soldier(Infantry())
    # army.add_soldier(Cavalry())
    # army.add_soldier(Infantry())
    # army.add_soldier(Cavalry())

    army.attack()
    # army.defend()

if __name__ == '__main__':
    main()