import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    
    def test_add_new_book_without_genre(self, collector):
        collector.add_new_book('Преступление и наказание')
        assert collector.get_book_genre('Преступление и наказание') == ''

    @pytest.mark.parametrize('name', ['Убить пересмешника', 'Три товарища', 'Война и мир'])
    def test_set_book_genre(self, collector, name):
        collector.add_new_book(name)
        collector.set_book_genre(name, 'Ужасы')
        assert collector.get_book_genre(name) == 'Ужасы'

    def test_get_book_genre_return_correct_genre(self, collector):
        collector.add_new_book('Убийство в Восточном экспрессе')
        collector.set_book_genre('Убийство в Восточном экспрессе', 'Детективы')
        genre = collector.get_book_genre('Убийство в Восточном экспрессе')
        assert genre == 'Детективы'

    def test_get_books_with_specific_genre_two_books(self,collector):
        collector.add_new_book('Мастер и Маргарита')
        collector.add_new_book('Три товарища')
        collector.set_book_genre('Мастер и Маргарита', 'Детективы')
        collector.set_book_genre('Три товарища', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Мастер и Маргарита','Три товарища']

    def test_get_books_genre_return_correct(self, collector):
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Дракула', 'Ужасы')
        assert collector.get_books_genre() == {
            'Шерлок Холмс': 'Детективы',
            'Дракула': 'Ужасы'}

    def test_get_books_for_children_without_rating(self, collector):
        collector.add_new_book('Волшебник Изумрудного города')
        collector.add_new_book('Дракула')
        collector.set_book_genre('Волшебник Изумрудного города', 'Фантастика')
        collector.set_book_genre('Дракула', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert books_for_children == ['Волшебник Изумрудного города']    
    
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert 'Война и мир' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert 'Война и мир' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_not_empty(self, collector):
        collector.add_new_book('Война и мир')
        collector.add_new_book('1984')
        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('1984')
        assert collector.get_list_of_favorites_books() == ['Война и мир', '1984']
