import pytest
from unittest.mock import patch
from io import StringIO
from main import commands


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
                    search_term in book['title'] or search_term in book[
                        'author'] or str(book['year']) == search_term]
        
        def display_books(self):
            return self.books
        
        def change_status(self, book_id, new_status):
            if 0 <= book_id < len(self.books):
                self.books[book_id]['status'] = new_status
    
    return MockLibrary()


def test_main_add_book(mock_library):
    with patch(
      'builtins.input', side_effect=['1', 'Книга 1', 'Автор 1', '2021', '0']
      ):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            commands()
            assert len(mock_library.books) == 1
            assert mock_library.books[0]['title'] == 'Книга 1'
            assert mock_library.books[0]['author'] == 'Автор 1'
            assert mock_library.books[0]['year'] == 2021


def test_main_search_book(mock_library):
    # First add a book
    mock_library.add_hook("Книга 1", "Автор 1", 2021)
    
    with patch('builtins.input', side_effect=['3', 'Книга 1', '0']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            commands()
            output = mock_stdout.getvalue()
            assert "ID: 0, Название: Книга 1" in output


def test_main_remove_book(mock_library):
    # Add a book first
    mock_library.add_hook("Книга 1", "Автор 1", 2021)
    
    with patch('builtins.input', side_effect=['2', '0', '0']):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            commands()
            assert len(mock_library.books) == 0

