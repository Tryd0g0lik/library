"""Test an interface by add a book"""
import pytest
from __tests__.buffers import buffer
from __tests__.test_main.parameters.parameters_main_add_book import testdata



@pytest.mark.parametrize(
    "command_start, title, author, year,\
 command_child, author_search, command_end, expect",
    testdata,
)
def test_main_add_book(
    command_start,
    title,
    author,
    year,
    command_child,
    author_search,
    command_end,
    expect,
):
    # Mock the input's data from user

    inputs = [
        command_start,
        title,
        author,
        year,
        command_child,
        author_search,
        command_end,
    ]
    
    output = buffer(inputs)
    assert expect in output




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
