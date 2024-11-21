"""
This is a file working only with the PostgreSQL db
"""
import psycopg2
from psycopg2 import sql

from dotenv_ import (APP_POSTGRES_LOGIN,
                     APP_POSTGRES_PASS,
                     APP_POSTGRES_DBNAME,
                     APP_POSTGRES_PORT,
                     APP_POSTGRES_HOST,)


def create_database_if_not_exsists(db_name: str)-> bool:
    """
    Def is only checking db. From entry point ('db_name') we receive a db name\
    and her will be look up in inside the postgresql. When returns the 'True' \
    it means what we have a db name or 'False'.
    :param db_name: str This is a db name.
    :return:bool.
    """
    connection = psycopg2.connect(user=f"{APP_POSTGRES_LOGIN}",
                                  password=f"{APP_POSTGRES_PASS}",
                                  host=f"{APP_POSTGRES_HOST}",
                                  port=f"{APP_POSTGRES_PORT}")
    connection.autocommit = True
    
