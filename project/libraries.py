"""Here is a logic for work with db"""
from project.models import (get_session, Books)

class Library:
    def __init__(self):
        self.session = get_session()
    
    def add_hook(self,
                 title: str,
                 author: str,
                 year: int,
                 status="в наличии") -> None:
        """
        TODO: Add a new bork
        :param title: str. This is a name book.
        :param author: str.
        :param year: int. This is a year when this is book was created.
        :param status: is "в наличии" or "выдана"
        :return:
        """
        if status != "в наличии" and status != "выдана":
            print(f"[Library]: Книга '{title}' не добавлена. Неизвестный статус.")
            return
        new_book = Books(
            title=title,
            author=author,
            year=year,
            status=status
        )
        self.session.add(new_book)
        self.session.commit()
        print(f"[Library]: Книга '{title}' добавлена.")
       
    def remove_book(self, book_id: int) -> None:
        """
        TODO: Here, we remove a book by book's index
        :param book_id: int.
        :return:
        """
        book = self.session.query(Books).filter_by(id=book_id)
        status_text = "None"
        if book:
            self.session.delete(book)
            self.session.commit()
            status_text.replace("None",
                                f"Книга с ID {book_id} удалена.")
        else:
            status_text.replace("None",
                                f"Книга с ID {book_id} не найдена.")
        print(f"[Library]: {status_text}")
    
    def find_books(self, search_term:str) -> list:
        """
        TODO: This is a method look up book by string's termns
        :param search_term: str. This is the title or author, or year
        :return:
        """
        results: list = self.session.query(Books).filter(
            (Books.title.ilike(f"%{search_term}%")) |
            (Books.author.ilike(f"%{search_term}%")) |
            (Books.year == int(search_term)
             if search_term.isdigit()
             else False)).all()
        return results
    
    def display_books(self) -> None:
        """
        TODO: Public an all books from library
        """
        books = self.session.query(Books).all()
        if not books:
            print("[Library]: Нет доступных книг.")
            return
        for book in books:
            print(f"[Library]: ID: {book.id}, Название: {book.title}, \
            Автор: {book.author}, Год: {book.year}, Статус: {book.status}")

    def change_status(self,
                      book_id: int,
                      new_status = "выдана"):
        """
        :param book_id: int
        :param new_status: str. Is "в наличии" or "выдана"
        :return:
        """
        if new_status != "в наличии" and new_status != "выдана":
            print(f"[Library]: Проверьте статус.")
            return
        book = self.session.query(Books).filter_by(id=book_id).first()
        if not book:
            print(f"[Library]: Книга с ID {book_id} не найдена. Проверьте ID")
            return
        if new_status in ["в наличии", "выдана"]:
            book.status = new_status
            self.session.commit()
            print(f"[Library]: Статус книги с ID {book_id} \
изменен на '{new_status}'.")