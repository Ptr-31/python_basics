# Напишите суперкласс Publisher (издательство) и два подкласса BookPublisher (книжное издательство) и NewspaperPublisher
# (газетное издательство).
#
# Родительский класс Publisher имеет два атрибута name и location (название, расположение) и два метода:
#
# get_info(self) – предоставляет информацию о названии и расположении издательства;
# publish(self, message) – выводит информацию об издании, которое находится в печати.
# Подклассы BookPublisher и NewspaperPublisher используют метод super().__init__(name, location) суперкласса для
# вывода информации о своих названии и расположении, и кроме того, имеют собственные атрибуты:
#
# BookPublisher – num_authors (количество авторов).
# NewspaperPublisher– num_pages (количество страниц в газете).

class Publisher:
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def get_info(self):
        return self.name, self.location
    def publish(self, edition):
        print('Готовим "' + edition + '" к публикации в', self.name, '(' + self.location + ')')
class BookPublisher(Publisher):
    def __init__(self, name, location, num_authors):
        super().__init__(name, location)
        self.num_authors = num_authors
    def publish(self, edition, author):
        print('Передаем рукопись \'' + edition + '\', написанную автором', author, 'в издательство', self.name, '('+ self.location + ')')

class NewspaperPublisher(Publisher):
    def __init__(self, name, location, num_pages):
        super().__init__(name, location)
        self.num_pages = num_pages
    def publish(self, article):
        print('Печатаем свежий номер со статьей "'+ article + '" на главной странице в издательстве', self.name, '('+ self.location + ')')
def main():
    publisher = Publisher("АБВГД Пресс", "Москва")
    publisher.publish("Справочник писателя")

    book_publisher = BookPublisher("Важные Книги", "Самара", 52)
    book_publisher.publish("Приключения Чебурашки", "В.И. Пупкин")

    newspaper_publisher = NewspaperPublisher("Московские вести", "Москва", 12)
    newspaper_publisher.publish("Новая версия Midjourney будет платной")


if __name__ == '__main__':
    main()