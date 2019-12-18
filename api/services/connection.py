import sqlite3
from sqlite3 import Error

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    
    return conn