# Parametrize
testdata = [['1',  # Команда добавить книгу
    'Книга 8',  # Название книги
    'Автор 8',  # Автор книги
    '2021',  # Год издания
    '3',  # Выбор показать все книги
    'Автор 8',  # Автор книги
    '0',  # Выход
    "Книга 8"] # Ожидаем ответ
    ,
    # Дублируем заголовок книги
    ['1', 'Книга 7', 'Автор 7', '2021', '3','Автор 7','0', 'Автор 7'],
    ['1', 'Книга 7', 'Автор 7', '2021', '3','Автор 7','0', "Error"],
    # Не верная команда
    ['11', 'Книга 7', 'Автор 7', '2021', '3','Автор 7','0',
     "Проверьте команду"],
    # Ограничение кол-ва сим-ов в строке
    ['1', '10', 'Автор 10', '2021', '3', 'Автор 10', '0', "Error"],
    ['1', 'Книга 12', '12', '2021', '3', '12', '0', "Error" ],
    ['1', 'Книга 13', 'Автор 13', '21', '3','Автор 13','0', "Error"],
    ['1', 'Книга 14', 'Автор 14', '2021', '3','14','0', 'Автор 14']
]