
from api.models import Term
from sqlite3 import Error
from api.services.connection import create_connection
import sqlite3
import json

def obtener_correcciones():
    lista = {'correcciones':[]}
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM api_correcciones")
 
    rows = cur.fetchall()

    for row in rows:
        correccion = {
            'id': row[0],
            'fecha': row[1],
            'fk_defensa': row[2]
        }
        lista['correcciones'].append(correccion)
    return lista

def crear_correccion(correccion):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()

    print(correccion)

    sql = "SELECT id FROM api_defensa WHERE codigo='{0}'".format(correccion['defensa'])
    cur.execute(sql)
    row = cur.fetchall()
    defensa = list(row[0])
    print(defensa)

    sql = "INSERT INTO api_correcciones(fecha,fk_defensa_id) VALUES ('{0}',{1})".format(correccion['fecha'],defensa[0])
    cur.execute(sql)
    conn.commit()

def actualizar_correccion(correccion):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "UPDATE api_correcciones SET fecha='{0}' WHERE id={1}".format(correccion['fecha'], correccion['id'])
    cur.execute(sql)
    conn.commit()

def eliminar_correccion(id):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "DELETE FROM api_correcciones WHERE id={0}".format(id)
    cur.execute(sql)
    conn.commit()
