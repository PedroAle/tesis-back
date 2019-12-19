from api.models import Term
from sqlite3 import Error
from api.services.connection import create_connection
import sqlite3
import json

def obtener_usuarios():
    lista = {'usuarios':[]}
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM api_usuario")
 
    rows = cur.fetchall()

    for row in rows:
        usuario = {
            'id': row[0],
            'cedula': row[1],
            'tipo': row[2],
            'primer_nombre': row[3],
            'segundo_nombre': row[4],
            'primer_apellido': row[5],
            'segundo_apellido': row[6],
            'correo_ucab': row[7],
            'correo_personal': row[8],
            'password': row[9],
            'telefono_uno': row[10],
            'telefono_dos': row[11],
            'observaciones': row[12]
        }
        lista['usuarios'].append(usuario)
    return lista

def obtener_usuario(id):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "SELECT * FROM api_usuario WHERE id={0}".format(id)
    cur.execute(sql)
 
    row = cur.fetchall()
    user = list(row[0])
    print(user)

    usuario = {
        'id': user[0],
        'cedula': user[1],
        'tipo': user[2],
        'primer_nombre': user[3],
        'segundo_nombre': user[4],
        'primer_apellido': user[5],
        'segundo_apellido': user[6],
        'correo_ucab': user[7],
        'correo_personal': user[8],
        'password': user[9],
        'telefono_uno': user[10],
        'telefono_dos': user[11],
        'observaciones': user[12]
    }
    return usuario
    
    

def crear_usuario(usuario):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}')'''.format(usuario['cedula'],usuario['tipo'],usuario['primer_nombre'],usuario['segundo_nombre'],usuario['primer_apellido'],usuario['segundo_apellido'],usuario['correo_ucab'],usuario['correo_personal'],usuario['password'],usuario['telefono_uno'],usuario['telefono_dos'],usuario['observaciones'])
    cur.execute(sql)
    conn.commit()

def actualizar_usuario(usuario):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = '''UPDATE api_usuario 
            SET cedula='{0}', tipo='{1}', primer_nombre='{2}', segundo_nombre='{3}', primer_apellido='{4}', segundo_apellido='{5}', correo_ucab='{6}', correo_personal='{7}', password='{8}', telefono_uno='{9}', telefono_dos='{10}', observaciones='{11}'
            WHERE id={12}'''.format(usuario['cedula'],usuario['tipo'],usuario['primer_nombre'],usuario['segundo_nombre'],usuario['primer_apellido'],usuario['segundo_apellido'],usuario['correo_ucab'],usuario['correo_personal'],usuario['password'],usuario['telefono_uno'],usuario['telefono_dos'],usuario['observaciones'],usuario['id'])
    cur.execute(sql)
    conn.commit()

def eliminar_usuario(id):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "DELETE FROM api_usuario WHERE id={0}".format(id)
    cur.execute(sql)
    conn.commit()
