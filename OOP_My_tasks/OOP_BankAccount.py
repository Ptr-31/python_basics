# Создайте класс BankAccount, который имеет следующие свойства:
#
# balance – приватный атрибут для хранения текущего баланса счета;
# interest_rate –приватный атрибут для процентной ставки;
# transactions – приватный атрибут для списка всех операций, совершенных по счету.
# Класс BankAccount должен иметь следующие методы:
#
# deposit(amount) – добавляет сумму к балансу и регистрирует транзакцию;
# withdraw(amount) – вычитает сумму из баланса и записывает транзакцию;
# add_interest() – добавляет проценты к счету на основе interest_rate и записывает транзакцию;
# history() – печатает список всех операций по счету.

class BankAccount:
    def __init__(self, balance, interest_rate):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount):
        # old_balance = self.__balance
        self.__balance += amount
        self.__transactions.append(f'Пополнение +{amount}, остаток на счете:{self.__balance}')
    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount
            self.__transactions.append(f'Снятие -{amount}, остаток на счете:{self.__balance}')
        else:
            print('Ошибка снятия, введенная сумма превышает остаток на счете')
    def add_interest(self):
        interests = self.__balance * self.__interest_rate
        self.__balance += interests
        self.__transactions.append(f'Начисление процентов по вкладу, +{self.__interest_rate}, начислены проценты по вкладу {interests}; остаток на счете:{self.__balance}')
    def history(self):
        for i in self.__transactions: print(i)
def main():
    account = BankAccount(100000, 0.05)

    # вносим 15 тысяч на счет
    account.deposit(15000)

    # снимаем 7500 рублей
    account.withdraw(7500)

    # начисляем проценты по вкладу
    account.add_interest()

    # печатаем историю операций
    account.history()
if __name__ == '__main__':
    main()