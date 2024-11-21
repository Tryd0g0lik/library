"""Here is a logic for work with db"""
from models import (get_session, Books)

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
        new_book = Books(
            title=title,
            author=author,
            year=year,
            status=status
        )
        self.session.add(new_book)
        self.session.commit()
        print(f"Книга '{title}' добавлена.")
       
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
        This is a method look up book by string's termns
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
    