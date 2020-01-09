from sqlite3 import Error
from api.services.connection import create_connection
from api.services.utils import isEmpty
import sqlite3
import json

def delete_data():
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()

    sql = '''Delete from api_correcciones'''
    cur.execute(sql)
    conn.commit()

    sql = '''Delete from api_defensa'''
    cur.execute(sql)
    conn.commit()

    sql = '''Delete from api_jurado'''
    cur.execute(sql)
    conn.commit()

    sql = '''Delete from api_trabajodegrado'''
    cur.execute(sql)
    conn.commit()

    sql = '''Delete from api_usuariopropuesta'''
    cur.execute(sql)
    conn.commit()

    sql = '''Delete from api_propuesta'''
    cur.execute(sql)
    conn.commit()

    sql = '''Delete from api_term'''
    cur.execute(sql)
    conn.commit()

    sql = '''Delete from api_usuario'''
    cur.execute(sql)
    conn.commit()

    conn.close()

delete_data()