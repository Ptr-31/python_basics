# Напишите класс Recipe с двумя методами:
#
# print_ingredients(self) – выводит список продуктов, необходимых для приготовления блюда;
# cook(self) – сообщает название выбранного рецепта и уведомляет о готовности блюда.

class Recipe:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
    def print_ingredients(self):
        print('Ингредиенты для', self.name + ':')
        for product in self.ingredients:
            print('–', product)
    def cook(self):
        print('Сегодня мы готовим', self.name)
        print('Выполняем инструкцию по приготовлению блюда Спагетти болоньезе...')
        print('Блюдо Спагетти болоньезе готово!')
def main():
    spaghetti = Recipe("Спагетти болоньезе", ["Спагетти", "Фарш", "Томатный соус", "Лук", "Чеснок", "Соль"])
    # печатаем список продуктов для рецепта спагетти
    spaghetti.print_ingredients()
    spaghetti.cook()

    cake = Recipe("Кекс", ["Мука", "Яйца", "Молоко", "Сахар", "Сливочное масло", "Соль", "Ванилин"])

    # печатаем рецепт кекса
    cake.print_ingredients()

    # готовим кекс
    cake.cook()
if __name__ == '__main__':
    main()