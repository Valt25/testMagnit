import os
import sqlite3


def populate_db(connection):
    try:
        with open(os.path.dirname(os.path.abspath(__file__)) + '/init.sql', 'r') as sql_file:
            cursor = connection.cursor()
            sql_statements = sql_file.read()
            cursor.executescript(sql_statements)
            connection.commit()
            cursor.close()
    except FileNotFoundError as e:
        print(e)
        raise e


def create_db(db_file):
    try:
        conn = sqlite3.connect(db_file)
        populate_db(conn)
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()


db_file_name = './db.sqlite3'
