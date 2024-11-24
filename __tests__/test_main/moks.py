"""
Это заглушка, для работы с фалом вместо базы данных. \
Файл есть земена базы данных. \
Данные получаем предварительно из буфера используя \
'from io import StringIO', 'from unittest.mock import patch'.

"Почему не использована заглушка?" Ответ в файле README - цель теста.
"""
import pytest
from io import StringIO
@pytest.fixture
def mock_console():
    test_stream = StringIO()
    with test_stream as ts:
        yield ts
        ts.close()

@pytest.fixture
def mock_library():
    """Fixture to mock the Library class."""

    class MockLibrary:
        def __init__(self):
            self.books = []

        def add_hook(self, title, author, year):
            self.books.append({'title': title, 'author': author, 'year': year})

        def remove_book(self, book_id):
            if 0 <= book_id < len(self.books):
                self.books.pop(book_id)

        def find_books(self, search_term):
            return [book for book in self.books if
                    search_term in book['title'] or search_term
                    in book['author'] or str(book['year']) == search_term]

        def display_books(self):
            return self.books

        def change_status(self, book_id, new_status):
            if 0 <= book_id < len(self.books):
                self.books[book_id]['status'] = new_status

    return MockLibrary()