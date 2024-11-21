"""Here is a logic for work with db"""
from models import (get_session, Books)

class Library:
    def __init__(self):
        self.session = get_session()
    
    def add_hook(self,
                 title: str,
                 author: str,
                 year: int,
                 status="в наличии"):
        pass