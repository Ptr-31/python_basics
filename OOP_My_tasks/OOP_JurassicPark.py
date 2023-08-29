# Палеонтологам, работающим в заповеднике для динозавров, понадобилось ПО для отслеживания множества травоядных и
# плотоядных подопечных. Данные, которые нужно учитывать по каждому динозавру – имя, вид, рост, вес и рацион питания.
#
# Создайте абстрактный класс Dinosaur с методами get_personal_name(), get_breed(), get_height(), get_weight() и get_diet().
# Затем создайте два подкласса Carnivore (плотоядный) и Herbivore (травоядный), которые наследуют методы Dinosaur и реализуют
# свои собственные версии get_personal_name(), get_breed(), get_height(), get_weight() и get_diet(). Кроме того, создайте класс
# DinosaurPark, который содержит список динозавров и имеет методы list_dinosaurs(), list_carnivores() и list_herbivores()
# для вывода списков a) всех динозавров, b) плотоядных и c) травоядных особей.

from abc import ABC, abstractmethod

class Dinasaur(ABC):
    @abstractmethod
    def get_personal_name(self):
        pass

    @abstractmethod
    def get_breed(self):
        pass

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass

    @abstractmethod
    def get_diet(self):
        pass

class Carnivore(Dinasaur):
    def __init__(self, breed, name, weight, height):
        self.__breed = breed
        self.__name = name
        self.__weight = weight
        self.__height = height

    def get_personal_name(self):
        return self.__name

    def get_breed(self):
        return self.__breed

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight

    def get_diet(self):
        return 'Плотоядный'

class Herbivore(Dinasaur):
    def __init__(self, breed, name, weight, height):
        self.__breed = breed
        self.__name = name
        self.__weight = weight
        self.__height = height

    def get_personal_name(self):
        return self.__name

    def get_breed(self):
        return self.__breed

    def get_height(self):
        return self.__height

    def get_weight(self):
        return self.__weight
    def get_diet(self):
        return 'Травоядный'

class DinosaurPark():
    dino = []

    def add_dinosaur(self, random_dino):
        self.dino.append(random_dino)

    def list_dinosaurs(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), dinosaur.get_height(), dinosaur.get_weight(),
                 dinosaur.get_diet())for dinosaur in self.dino]

    def list_carnivores(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), dinosaur.get_height(), dinosaur.get_weight(),
                 dinosaur.get_diet()) for dinosaur in self.dino if isinstance(dinosaur, Carnivore)]

    def list_herbivores(self):
        return [(dinosaur.get_personal_name(), dinosaur.get_breed(), dinosaur.get_height(), dinosaur.get_weight(), dinosaur.get_diet()) for
                dinosaur in self.dino if isinstance(dinosaur, Herbivore)]

def main():
    t_rex = Carnivore('Тираннозавр', 'Рекс', 4800, 560)
    velociraptor = Carnivore('Велоцираптор', 'Зубастик', 30, 70)
    stegosaurus = Herbivore('Стегозавр', 'Стегга', 7100, 420)
    triceratops = Herbivore('Трицератопс', 'Трипси', 8000, 290)

    park = DinosaurPark()

    park.add_dinosaur(t_rex)
    park.add_dinosaur(velociraptor)
    park.add_dinosaur(stegosaurus)
    park.add_dinosaur(triceratops)


    for dinosaur in park.list_dinosaurs():
        print(f'Имя: {dinosaur[0]}\n'
              f'Вид: {dinosaur[1]}\n'
              f'Вес: {dinosaur[2]} кг\n'
              f'Рост: {dinosaur[3]} см\n'
              f'Рацион: {dinosaur[4]}\n')


if __name__ == '__main__':
    main()

