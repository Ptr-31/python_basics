# Для игры, посвященной этой войне, нужно создать абстрактный класс Starship с методами warp_speed(), fire_weapon() и
# self_destruct(). Кроме того, нужно создать два подкласса FederationStarship и KlingonWarship, которые наследуют абстрактные
# методы Starship и реализуют свои собственные версии методов warp_speed(), fire_weapon() и self_destruct().

from abc import ABC, abstractmethod

class Starship(ABC):
    @abstractmethod
    def warp_speed(self):
        pass

    @abstractmethod
    def fire_weapon(self):
        pass

    @abstractmethod
    def self_destruct(self):
        pass
class FederationStarship(Starship):
    def warp_speed(self):
        print('Включить варп-двигатели!')

    def fire_weapon(self):
        print('Выпустить фотонные торпеды!')

    def self_destruct(self):
        print('Запускаю систему самоуничтожения!')

class KlingonWarship(Starship):
    def warp_speed(self):
        print('Включить маскировочное устройство!')

    def fire_weapon(self):
        print('Стрелять из фазеров!')

    def self_destruct(self):
        print('Запускаю систему самоуничтожения!')

def main():
    enterprise = FederationStarship()
    bird_of_prey = KlingonWarship()

    enterprise.warp_speed()
    bird_of_prey.warp_speed()

    enterprise.fire_weapon()
    bird_of_prey.fire_weapon()

    enterprise.self_destruct()
    bird_of_prey.self_destruct()

if __name__ == '__main__':
    main()