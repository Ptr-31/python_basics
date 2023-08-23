class Vehicle:
    def __init__(self, manufacture, model, year, price):
        self.manufacture = manufacture
        self.model = model
        self.year = year
        self.price = price
    def display_info(self):
        print(self.manufacture, self.model, self.year, str(self.price) + '$')
class Truck(Vehicle):
    def __init__(self, manufacture, model, year, price, power, volume):
        super().__init__(manufacture, model, year, price)
        self.__power = power
        self.volume = volume
    def display_info(self):
        print(self.manufacture, self.model, self.year, str(self.price) + '$', str(self.__power) + 'hp', 'volume = ' + str(self.volume))

def main():
    Aston = Vehicle('Aston Martin', 'DBS', 2018, 200000)
    Aston.display_info()
    Volvo = Truck('Volvo', 'DX-1', 2018, 150000, 719, 0)
    Volvo.display_info()
if __name__ == '__main__':
    main()