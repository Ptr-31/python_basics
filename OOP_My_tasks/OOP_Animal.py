# Напишите класс Animal, обладающий свойствами name, species, legs, в которых хранятся данные о кличке, виде и
# количестве ног животного. Класс также должен иметь два метода – voice() и move(), которые сообщают о
# том, что животное подает голос и двигается.
#
# Создайте два подкласса – Dog и Bird. Подкласс Dog имеет атрибут breed (порода) и метод bark(), который сообщает о том, что
# собака лает. Подкласс Bird обладает свойством wingspan (размах крыльев) и методом fly(), который уведомляет о полете птицы.

class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs
    def voice(self):
        print(f'{self.name} подает голос')
    def move(self):
        print(f'{self.name} двигает хвостом')

class Dog(Animal):
    def __init__(self,name, breed, legs):
        super().__init__(name, breed, legs)
        self.breed = breed
    def bark(self):
        print(f'{self.breed} {self.name} лает')
class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species, 2)
        self.wingspan = wingspan
    def fly(self):
        print(f'{self.species} {self.name} летает')
def main():
    dog = Dog("Геральт", "доберман", 4)
    bird = Bird("Вася", "попугай", 2)
    dog.voice()
    bird.voice()
    dog.move()
    bird.move()
    dog.bark()
    bird.fly()
if __name__ == '__main__':
    main()