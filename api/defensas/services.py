
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

def obtener_defensa(id):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "SELECT * FROM api_defensa WHERE id={0}".format(id)
    cur.execute(sql)
 
    row = cur.fetchall()
    defen = list(row[0])
    print(defen)

    sql = "SELECT fk_usuario_id FROM api_jurado WHERE fk_defensa_id={0}".format(id)
    cur.execute(sql)
    row = cur.fetchall()
    jurado_1 = list(row[0])
    jurado_2 = list(row[1])
    jurado_3 = list(row[2])
    print(jurado_1[0])

    sql = "SELECT primer_nombre, primer_apellido, cedula, tipo FROM api_usuario WHERE id={0}".format(jurado_1[0])
    cur.execute(sql)
    row = cur.fetchall()
    jurado_1_datos = list(row[0])
    print(jurado_1_datos)

    sql = "SELECT primer_nombre, primer_apellido, cedula, tipo FROM api_usuario WHERE id={0}".format(jurado_2[0])
    cur.execute(sql)
    row = cur.fetchall()
    jurado_2_datos = list(row[0])
    print(jurado_2_datos)

    sql = "SELECT primer_nombre, primer_apellido, cedula, tipo FROM api_usuario WHERE id={0}".format(jurado_3[0])
    cur.execute(sql)
    row = cur.fetchall()
    jurado_3_datos = list(row[0])
    print(jurado_3_datos)

    defensa = {
        'id': defen[0],
        'codigo': defen[1],
        'fecha_hora':defen[2],
        'calificacion':defen[3],
        'mencion_publicacion':defen[4],
        'mencion_honorifica': defen[5],
        'nota': defen[6],
        'jurados': [{
            'primer_nombre': jurado_1_datos[0],
            'primer_apellido': jurado_1_datos[1],
            'cedula': jurado_1_datos[2],
            'tipo': ''
        },
        {
            'primer_nombre': jurado_2_datos[0],
            'primer_apellido': jurado_2_datos[1],
            'cedula': jurado_2_datos[2],
            'tipo': ''
        },
        {
            'primer_nombre': jurado_2_datos[0],
            'primer_apellido': jurado_2_datos[1],
            'cedula': jurado_2_datos[2],
            'tipo': 'Suplente'
        }]
    }
    return defensa

def obtener_defensas_no_realizadas():
    lista = {'defensas':[]}
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = '''
            select u.cedula as Cedula, u.primer_apellido || ' ' || u.segundo_apellido as Apellidos, u.primer_nombre || ' ' || u.segundo_nombre as Nombres, t.term, tg.titulo, d.fecha_hora
            from api_usuario as u, api_term as t, api_propuesta as p, api_usuariopropuesta as up, api_trabajodegrado as tg, api_defensa as d
            where tg.estatus = 'Aprobada' and p.id = up.fk_propuesta_id and u.id = up.fk_usuario_id and p.fk_term_id = t.id and u.tipo = 'Estudiante' and p.id = tg.fk_propuesta_id and d.fk_trabajo_grado_id = tg.id and datetime('now') < d.fecha_hora
            order by u.cedula
        '''
    cur.execute(sql)
 
    rows = cur.fetchall()

    for row in rows:
        defensa = {
            'cedula': row[0],
            'apellidos': row[1],
            'nombres':row[2],
            'term':row[3],
            'trabajodegrado':row[4],
            'fecha_hora': row[5]
        }
        lista['defensas'].append(defensa)
    return lista

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

    sql = "SELECT id FROM api_defensa WHERE codigo='{0}'".format(defensa['codigo'])
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_defensa = row[0]
    print(id_defensa)

    sql = "INSERT INTO api_jurado(fk_defensa_id,fk_usuario_id,suplente) VALUES ('{0}','{1}',0)".format(id_defensa,id_jurado_uno)
    cur.execute(sql)
    conn.commit()

    sql = "INSERT INTO api_jurado(fk_defensa_id,fk_usuario_id,suplente) VALUES ('{0}','{1}',0)".format(id_defensa,id_jurado_dos)
    cur.execute(sql)
    conn.commit()

    sql = "INSERT INTO api_jurado(fk_defensa_id,fk_usuario_id,suplente) VALUES ('{0}','{1}',1)".format(id_defensa,id_jurado_tres)
    cur.execute(sql)
    conn.commit()
    
def actualizar_defensa(defensa):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = '''UPDATE api_defensa
            SET codigo='{0}', fecha_hora='{1}', calificacion={2}, mencion_publicacion={3}, mencion_honorifica={4}, nota={5}
            WHERE id={6}'''.format(defensa['codigo'],defensa['fecha_hora'],defensa['calificacion'],defensa['mencion_publicacion'],defensa['mencion_honorifica'],defensa['nota'],defensa['id'])
    cur.execute(sql)
    conn.commit()

    if(not isEmpty(defensa['jurado_uno'])):

        sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format(defensa['jurado_uno'])
        cur.execute(sql)
        row = list(cur.fetchall()[0])
        id_jurado_uno = row[0]
        print(id_jurado_uno)

        sql = '''UPDATE api_jurado
            SET fk_usuario_id={0}
            WHERE fk_defensa_id={1}'''.format(id_jurado_uno,defensa['id'])
        cur.execute(sql)
        conn.commit()

    if(not isEmpty(defensa['jurado_dos'])):

        sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format(defensa['jurado_dos'])
        cur.execute(sql)
        row = list(cur.fetchall()[0])
        id_jurado_dos = row[0]
        print(id_jurado_dos)

        sql = '''UPDATE api_jurado
            SET fk_usuario_id={0}
            WHERE fk_defensa_id={1}'''.format(id_jurado_dos,defensa['id'])
        cur.execute(sql)
        conn.commit()

    if(not isEmpty(defensa['jurado_tres'])):

        sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format(defensa['jurado_tres'])
        cur.execute(sql)
        row = list(cur.fetchall()[0])
        id_jurado_tres = row[0]
        print(id_jurado_tres)

        sql = '''UPDATE api_jurado
            SET fk_usuario_id={0}
            WHERE fk_defensa_id={1}'''.format(id_jurado_tres,defensa['id'])
        cur.execute(sql)
        conn.commit()

def eliminar_defensa(id):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "DELETE FROM api_defensa WHERE id={0}".format(id)
    cur.execute(sql)
    conn.commit()
    sql = "DELETE FROM api_jurado WHERE fk_defensa_id={0}".format(id)
    cur.execute(sql)
    conn.commit()
