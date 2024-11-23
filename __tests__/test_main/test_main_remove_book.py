"""Test an interface by remove a book"""

from io import StringIO
from unittest.mock import patch

import pytest

from __tests__.test_main.parameters.parameters_main_remove_book import \
  testdata_remove
from main import commands


@pytest.mark.parametrize("command1, idbook, command2, expect", testdata_remove)
def test_main_remove_book(command1, idbook, command2, expect):
    """
    TODO: This is test function for check an interface from the Library/
        Now will be testing the function book's remove
    :param command1:
    :param idbook:
    :param command2:
    :param expect:
    :return:
    """
    inputs = [command1, idbook, command2]
    with patch("builtins.input", side_effect=inputs), patch(
        "sys.stdout", new_callable=StringIO
    ) as mock_stdout:
        commands()
        # Received data after input text
        output = mock_stdout.getvalue()
        assert expect in output
