from sqlite_orm.database import Database
from api.models import Usuario
import sqlite3
from sqlite3 import Error
import json

def create_connection(database):
    conn = None
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error as e:
        print(e)
    
    return conn

def obtener_usuarios():
    
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    """ cur.execute("INSERT INTO api_term(term) VALUES ('2221')")
    conn.commit() """
    cur.execute("SELECT * FROM api_usuarios")
 
    rows = cur.fetchall()

    for row in rows:
        usuario = {
            'id': row[0],
            'cedula':row[1],
            'tipo': row[2],
            'primer_nombre': row[3],
            'segundo_nombre': row[4],
            'primer_apellido': row[5],
            'segundo_apellido': row[6],
            'correo_ucab': row[7],
            'correo_personal':row[8],
            'telefono_uno': row[9],
            'telefono_dos': row[10],
            'observaciones': row[11]
        }
        lista['usuarios'].append(usuario)
    return lista

lista = {'usuarios':[]}