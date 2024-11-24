"""Test an interface by remove a book"""

from io import StringIO
from unittest.mock import patch

import pytest

from __tests__.buffers import buffer
from __tests__.test_main.parameters.parameters_main_remove_book import \
  testdata_remove
from main import commands


@pytest.mark.parametrize("command1, idbook, command2, expect", testdata_remove)
def test_main_remove_book(command1: [str, int],
                          idbook: [str, int],
                          command2: [str, int], expect: str) -> None:
    """
    TODO: This is test function for check an interface from the Library/
        Now will be testing the function book's remove
    :param command1: [str, int]. First command.
    :param idbook: [str, int]. This id of book for search in db.
    :param command2: [str, int]. Completed.
    :param expect: str. Expected result`
    :return:
    """
    inputs = [command1, idbook, command2]
    output = buffer(inputs)
    assert expect in output
