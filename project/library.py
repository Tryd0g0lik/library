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
        pass