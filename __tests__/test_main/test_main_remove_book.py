#
# def test_main_remove_book(mock_library):
#     # Add a book first
#     mock_library.add_hook("Книга 1", "Автор 1", 2021)
#
#     with patch('builtins.input', side_effect=['2', '0', '0']):
#         with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#             commands()
#             assert len(mock_library.books) == 0
#
