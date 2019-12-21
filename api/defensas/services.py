
from api.models import Term
from sqlite3 import Error
from api.services.connection import create_connection
import sqlite3
from api.services.utils import isEmpty, generateError, successAction, isNumber 
import json

def obtener_defensas():
    lista = {'defensas':[]}
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM api_defensa")
 
    rows = cur.fetchall()

    for row in rows:
        defensa = {
            'id': row[0],
            'codigo': row[1],
            'fecha_hora':row[2],
            'calificacion':row[3],
            'mencion_publicacion':row[4],
            'mencion_honorifica': row[5],
            'nota': row[6],
            'fk_trabajo_grado': row[7]
        }
        lista['defensas'].append(defensa)
    return lista

def obtener_propuesta(id):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "SELECT * FROM api_propuesta WHERE id={0}".format(id)
    cur.execute(sql)
 
    row = cur.fetchall()
    propue = list(row[0])
    print(propue)

    sql = "SELECT term FROM api_term WHERE id={0}".format(propue[5])
    cur.execute(sql)
    row = cur.fetchall()
    term = list(row[0])
    print(term)

    propuesta = {
        'id': propue[0],
        'codigo': propue[1],
        'fecha_entrega':propue[2],
        'titulo':propue[3],
        'estatus':propue[4],
        'fk_term': term[0]
    }
    return propuesta

def crear_defensa(defensa):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()

    sql = "SELECT id FROM api_trabajodegrado WHERE codigo='{0}'".format(defensa['trabajodegrado'])
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_trabajodegrado = row[0]
    print(id_trabajodegrado)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format(defensa['jurado_uno'])
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_jurado_uno = row[0]
    print(id_jurado_uno)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format(defensa['jurado_dos'])
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_jurado_dos = row[0]
    print(id_jurado_dos)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format(defensa['jurado_tres'])
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_jurado_tres = row[0]
    print(id_jurado_tres)

    sql = "INSERT INTO api_defensa(codigo,fecha_hora,calificacion,mencion_publicacion,mencion_honorifica,nota,fk_trabajo_grado_id) VALUES ('{0}','{1}','{2}',{3},{4},{5},{6})".format(defensa['codigo'],defensa['fecha_hora'],defensa['calificacion'],defensa['mencion_publicacion'],defensa['mencion_honorifica'],defensa['nota'],id_trabajodegrado)
    cur.execute(sql)
    conn.commit()

    sql = "INSERT INTO api_jurado(fk_defensa_id,fk_usuario_id,suplente) VALUES ('{0}','{1}',False)".format(id_propuesta,id_jurado_uno)
    cur.execute(sql)
    conn.commit()

    sql = "INSERT INTO api_jurado(fk_defensa_id,fk_usuario_id,suplente) VALUES ('{0}','{1}',False)".format(id_propuesta,id_jurado_dos)
    cur.execute(sql)
    conn.commit()

    sql = "INSERT INTO api_jurado(fk_defensa_id,fk_usuario_id,suplente) VALUES ('{0}','{1}',True)".format(id_propuesta,id_jurado_tres)
    cur.execute(sql)
    conn.commit()
    
def actualizar_propuesta(propuesta):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = '''UPDATE api_propuesta 
            SET codigo='{0}', fecha_entrega='{1}', titulo='{2}', estatus='{3}', fk_term_id='{4}'
            WHERE id={5}'''.format(propuesta['codigo'],propuesta['fecha_entrega'],propuesta['titulo'],propuesta['estatus'],propuesta['fk_term'],propuesta['id'])
    cur.execute(sql)
    conn.commit()

def eliminar_propuesta(id):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "DELETE FROM api_propuesta WHERE id={0}".format(id)
    cur.execute(sql)
    conn.commit()
    sql = "DELETE FROM api_usuariopropuesta WHERE id={0}".format(id)
    cur.execute(sql)
    conn.commit()
