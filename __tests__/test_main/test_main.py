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
