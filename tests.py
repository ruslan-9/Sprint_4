import pytest

class TestBooksCollector:
    
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
        collector.add_new_book('Десять негритят')
        collector.set_book_genre('Мастер и Маргарита', 'Роман')
        collector.set_book_genre('Три товарища', 'Детективы')
        collector.set_book_genre('Десять негритят', 'Детективы')
        assert collector.get_books_with_specific_genre('Детективы') == ['Три товарища', 'Десять негритят']

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
