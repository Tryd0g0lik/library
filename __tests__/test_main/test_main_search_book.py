"""Test an interface by search a book(s)"""
import pytest

from __tests__.buffers import buffer
from __tests__.test_main.parameters.parameters_main_search_book import \
    testdata_search


@pytest.mark.parametrize(
    "command_start, search_data, command_end, expect",
    testdata_search,
)
def test_main_search_book(command_start, search_data, command_end, expect):
    inputs = [command_start, search_data, command_end,]
    output = buffer(inputs)
    assert expect in output
