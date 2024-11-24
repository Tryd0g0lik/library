"""Test an interface by search a book(s)"""
import pytest

from __tests__.buffers import buffer
from __tests__.test_main.parameters.parameters_main_search_book import \
    testdata_search


@pytest.mark.parametrize(
    "command_start, search_data, command_end, expect",
    testdata_search,
)
def test_main_search_book(command_start: [str, int],
                          search_data: str,
                          command_end: [str, int], expect: str) -> None:
    """
    :param command_start: [str, int]. First command.
    :param search_data: str. Data - what will have a search.
    :param command_end: [str, int]. Child command between a search and \
the search's result.
    :param expect: str. Expected result
    :return:
    """
    inputs = [command_start, search_data, command_end,]
    output = buffer(inputs)
    assert expect in output
