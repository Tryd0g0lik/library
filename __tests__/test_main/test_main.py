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
    command_start:[str, int],
    title: str,
    author: str,
    year:[str, int],
    command_child: [str, int],
    author_search: str,
    command_end: [str, int],
    expect: str,
) -> None:
    """
    
    :param command_start: [str, int]. First command.
    :param title: str. Name of new book
    :param author: : str. Author of new book
    :param year: [str, int], When was created a new book
    :param command_child: [str, int] In db will add \
 new position. Child command between a search and the search's result.
    :param author_search: str. Data - what will have a search, after.
    :param command_end: [str, int]. Complete.
    :param expect: str. Expected result`
    :return:
    """
    
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
