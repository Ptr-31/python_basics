# Для учета музыкальных инструментов в оркестре нужно создать абстрактный класс Instrument с методами get_name(),
# get_type(), get_sound() и play(). Два подкласса StringedInstrument (струнные) и PercussionInstrument (ударные)
# наследуют методы Instrument и реализуют свои собственные версии методов get_name(), get_type(), get_sound() и play().
# Кроме того, необходимо реализовать класс Orchestra: он добавляет новые инструменты и имеет методы list_instruments(),
# list_stringed_instruments(), list_percussion_instruments(), которые выводят списки a) всех инструментов, b) ударных, c) струнных.

from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_sound(self):
        pass

    @abstractmethod
    def play(self):
        pass

class StringedInstrument(Instrument):
    def __init__(self, name, type, action):
        self.__name = name
        self.__type = type
        self.__action = action

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_sound(self):
        return self.__action

    def play(self):
        return f'Звучит {self.__type} {self.__name}'

class PercussionInstrument(Instrument):
    def __init__(self, name, type, action):
        self.__name = name
        self.__type = type
        self.__action = action

    def get_name(self):
        return self.__name

    def get_type(self):
        return self.__type

    def get_sound(self):
        return self.__action

    def play(self):
        return f'Звучит {self.__type} {self.__name}'

class Orchestra:
    __list_all = []
    __list_of_stringed = []
    __list_of_percussion = []

    def add_instrument(self, instrument):
        self.__list_of_stringed.append(instrument.get_name())
        if isinstance(instrument, StringedInstrument):
            self.__list_of_stringed.append(instrument.get_name())
        elif isinstance(instrument, PercussionInstrument):
            self.__list_of_percussion.append(instrument.get_name())
        else:
            print('Ошибка! Инструмент не соответствует ни одному классу.')
    def list_instruments(self):
        return self.__list_all

    def list_stringed_instruments(self):
        return self.__list_of_stringed

    def list_percussion_instruments(self):
        return self.__list_of_percussion

def main():
    chello = StringedInstrument("виолончель", "струнный инструмент", "Strum")
    maracas = PercussionInstrument("маракасы", "ударный инструмент", "Maracas")
    violin = StringedInstrument("скрипка", "струнный инструмент", "Virtuso")
    drums = PercussionInstrument("барабан", "ударный инструмент", "Beat")

    orchestra = Orchestra()
    orchestra.add_instrument(chello)
    orchestra.add_instrument(maracas)
    orchestra.add_instrument(violin)
    orchestra.add_instrument(drums)

    print("В оркестрe есть инструменты:", ', '.join(orchestra.list_instruments()))
    print("Струнные инструменты:", ', '.join(orchestra.list_stringed_instruments()))
    print("Ударные инструменты:", ', '.join(orchestra.list_percussion_instruments()))

    print(chello.play())
    print(drums.play())

if __name__ == '__main__':
    main()
