# def test_main_search_book(mock_library):
#     # First add a book
#     mock_library.add_hook("Книга 1", "Автор 1", 2021)
#
#     with patch('builtins.input', side_effect=['3', 'Книга 1', '0']):
#         with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#             commands()
#             output = mock_stdout.getvalue()
#             assert "ID: 0, Название: Книга 1" in output
#