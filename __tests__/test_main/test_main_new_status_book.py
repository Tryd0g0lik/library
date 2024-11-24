"""Test an interface by change a status book"""
import pytest

from __tests__.buffers import buffer
from __tests__.test_main.parameters.parameters_main_new_status_book import \
    testdata_status


@pytest.mark.parametrize(
    "command_start, idbook, status, command_child, search, command_end, expect",
    testdata_status,
)
def test_main_search_book(command_start: [str, int], idbook: [str, int],
                          status: str, command_child: [str, int],
                          search: str, command_end: [str, int],
                          expect: str) -> None:
    """
    TODO: Thi is a test for interface the book search.
    :param command_start: [str, int]    . First command.
    :param idbook: [str, int]. This id of book for search in db.
    :param status: str. New status.
    :param command_child: [str, int]. In db will be to look up our \
 old position.  Child command between a search and the search's result.
    :param search: str. Data - what will have a search.
    :param command_end: [str, int]. Complete.
    :param expect: str. Expected result`
    :return:
    """
    inputs = [command_start, idbook, status, command_child, search, command_end]
    output = buffer(inputs)
    assert expect in output
