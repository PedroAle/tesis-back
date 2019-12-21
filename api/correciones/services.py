
from api.models import Term
from sqlite3 import Error
from api.services.connection import create_connection
import sqlite3
import json

def obtener_correciones():
    lista = {'correciones':[]}
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM api_term")
 
    rows = cur.fetchall()

    for row in rows:
        correcion = {
            'id': row[0],
            'fecha': row[1]
        }
        lista['correcciones'].append(correcion)
    return lista

def crear_correcion(fecha):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "INSERT INTO api_correciones(fecha) VALUES ('{}')".format(fecha)
    cur.execute(sql)
    conn.commit()

def actualizar_term(data):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "UPDATE api_term SET term='{0}' WHERE id={1}".format(data['term'], data['id'])
    cur.execute(sql)
    conn.commit()

def eliminar_term(id):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "DELETE FROM api_term WHERE id={0}".format(id)
    cur.execute(sql)
    conn.commit()
