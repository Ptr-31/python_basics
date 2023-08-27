# Для военной игры-стратегии нужно написать класс Soldier (солдат). Класс имеет атрибуты name, rank и service_number
# (имя, воинское звание, порядковый номер), причем звание и номер – приватные свойства.
#
# Напишите методы для:
#
# получения воинского звания;
# подтверждения порядкового номера;
# повышения в звании;
# понижения в звании.
# Кроме того, нужно создать декоратор для вывода информации о персонаже.

RANKS = ["рядовой", "ефрейтор", "младший сержант", "сержант", "старший сержант",
         "прапорщик", "старший прапорщик"]


class Soldier():
    def __init__(self, name, rank, service_number):
        self.name = name
        self.__rank = rank
        self.__service_number = service_number
        print(f"Создан новый игровой персонаж типа {Soldier.__name__} с атрибутами: {self.__dict__}")

    def getter_rank(self):
        print(f'Персонаж {self.name} имеет звание {self.__rank}')

    def promote(self):
        if self.__rank in RANKS[:-1]:
            self.__rank = RANKS[RANKS.index(self.__rank) + 1]
            print(f'Персонаж {self.name} повышен в звании, теперь он {self.__rank}')
        elif self.__rank == RANKS[-1]:
            print(f'Дальше персонажа {self.name} повышать нельзя, он имеет максимальное звание!')
        else:
            print('Вы ввели некорректной звание!')

        # current_rate = RANKS.index(self.__rank)
        # if current_rate + 1 > len(RANKS) - 1:
        #     print(f'Дальше персонажа {self.name} повышать нельзя, он имеет максимальное звание!')
        # else:
        #     self.__rank = RANKS[current_rate + 1]
        # print(f'Персонаж {self.name} повышен в звании, теперь он {self.__rank}')

    def demote(self):
        if self.__rank in RANKS[1:]:
            self.__rank = RANKS[RANKS.index(self.__rank) - 1]
            print(f'Персонаж {self.name} понижен в звании, теперь он {self.__rank}')
        elif self.__rank == RANKS[0]:
            print(f'Дальше персонажа {self.name} понижать нельзя, он имеет минимальное звание!')
        else:
            print('Вы ввели некорректной звание!')

def main():
    soldier1 = Soldier("Иван Сусанин", "рядовой", "12345")
    soldier1.getter_rank()
    soldier1.promote()
    soldier1.demote()
if __name__ == '__main__':
    main()