"""
This is a sub function for the all tests.\
His works through lib.: unittest, io
"""
from io import StringIO
from unittest.mock import patch
from main import commands

def buffer(inputs: list) -> None:
    """
    Here, enter the input data to the input forms and receives results
    :param inputs: This is the list data of the actions over the input form.
    :return:
    """
    with patch("builtins.input", side_effect=inputs), patch(
      "sys.stdout", new_callable=StringIO
    ) as mock_stdout:
        """
        'builtins.input' - заглушка. 'side_effect' - данные для ввода
        'stdout' - получение из input
        'StringIO' - память для сохранения потока данных
        (mock_stdout.getvalue()) - '.getvalue()' получаем данные из 'StringIO'
        """
        # Run the library's logic
        commands()
        # Received data after input text/
        output = mock_stdout.getvalue()
    return output