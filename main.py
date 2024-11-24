"""Here is the manager of library app"""
from project.libraries import Library


def commands():
    """
    This is the manager of library app
    :return:
    """
    library = Library()
    status = True
    while status:
        print("\nМеню управления библиотекой:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Искать книгу")
        print("4. Показать все книги")
        print("5. Изменить статус книги")
        print("0. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора: ")
            year = int(input("Введите год издания: "))
            # CHECK
            if len(author) == 0:
                author = "anonim"
            if len(str(year)) == 0 or len(title) == 0:
                print("Не все поля заполнены.")
                status = False
                return status

            library.add_hook(title, author, year)

        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")
            library.remove_book(book_id)

        elif choice == "3":
            search_term = input("Введите название, автора или год для поиска: ")
            results = library.find_books(search_term)
            if results:
                for book in results:
                    print(
                        f"ID: {book.id}, Название: {book.title}, Автор: {book.author}, Год: {book.year}, Статус: {book.status}"
                    )
            else:
                print("Книги не найдены.")

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            book_id = input("Введите ID книги для изменения статуса: ")
            new_status = input("Введите новый статус (в наличии/выдана): ")
            library.change_status(book_id, new_status)

        elif choice == "0":
            library.close()
            break
        else:
            print("Проверьте команду.")


if __name__ == "__main__":
    commands()
