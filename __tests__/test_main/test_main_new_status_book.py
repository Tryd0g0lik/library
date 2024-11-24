"""Test an interface by change a status book"""
import pytest

from __tests__.buffers import buffer
from __tests__.test_main.parameters.parameters_main_new_status_book import \
    testdata_status


@pytest.mark.parametrize(
    "command_start, idbook, status, command_child, search, command_end, expect",
    testdata_status,
)
def test_main_search_book(command_start, idbook, status, command_child,
                          search, command_end, expect):
    inputs = [command_start, idbook, status, command_child, search, command_end]
    output = buffer(inputs)
    assert expect in output
