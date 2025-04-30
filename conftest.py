import pytest
from main import BooksCollector

@pytest.fixture  # Фикстура для создания экземпляра класса BooksCollector
def collector():
    return BooksCollector()
