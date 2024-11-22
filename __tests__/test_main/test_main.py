import pytest
from unittest.mock import patch
from io import StringIO
from main import commands




def test_main_add_book(mock_library, mock_console):
    # Мокируем ввод пользователя
    
    
    with patch('builtins.input', side_effect=inputs), \
      patch('sys.stdout', new_callable=StringIO) as mock_stdout:
        """
        'builtins.input' - заглушка. 'side_effect' - данные для ввода
        'stdout' - получение из input
        'StringIO' - память для сохранения потока данных
        (mock_stdout.getvalue()) - '.getvalue()' получаем данные из 'StringIO'
        """
        commands()  # Запуск функции
        
        output = mock_stdout.getvalue()  # Получаем вывод функции
    
    assert "Название: Книга 7" in output  #




# @pytest.fixture
# def mock_console():
#     test_stream = StringIO()
#     with test_stream as ts:
#         yield ts
#         ts.close()
#
# @pytest.fixture
# def mock_library():
#     """Fixture to mock the Library class."""
#
#     class MockLibrary:
#         def __init__(self):
#             self.books = []
#
#         def add_hook(self, title, author, year):
#             self.books.append({'title': title, 'author': author, 'year': year})
#
#         def remove_book(self, book_id):
#             if 0 <= book_id < len(self.books):
#                 self.books.pop(book_id)
#
#         def find_books(self, search_term):
#             return [book for book in self.books if
#                     search_term in book['title'] or search_term
#                     in book['author'] or str(book['year']) == search_term]
#
#         def display_books(self):
#             return self.books
#
#         def change_status(self, book_id, new_status):
#             if 0 <= book_id < len(self.books):
#                 self.books[book_id]['status'] = new_status
#
#     return MockLibrary()
#
# async def fill_feields(command,  expect):