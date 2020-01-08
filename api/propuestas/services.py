
from api.models import Term
from sqlite3 import Error
from api.services.connection import create_connection
import sqlite3
from api.services.utils import isEmpty, generateError, successAction, isNumber 
import json

def obtener_propuestas():
    lista = {'propuestas':[]}
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM api_propuesta")
 
    rows = cur.fetchall()

    for row in rows:
        propuesta = {
            'id': row[0],
            'codigo': row[1],
            'fecha_entrega':row[2],
            'titulo':row[3],
            'estatus':row[4],
            'fk_term': row[5]
        }
        lista['propuestas'].append(propuesta)
    return lista

def obtener_propuestas_no_aprobada():
    lista = {'propuestas':[]}
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = '''
            select u.cedula as Cedula, u.primer_apellido || ' ' || u.segundo_apellido as Apellidos, u.primer_nombre || ' ' || u.segundo_nombre as Nombres, t.term, p.titulo, p.estatus
            from api_usuario as u, api_term as t, api_propuesta as p, api_usuariopropuesta as up
            where p.estatus <> 'Aprobada' and p.id = up.fk_propuesta_id and u.id = up.fk_usuario_id and p.fk_term_id = t.id and u.tipo = 'Estudiante'
            order by u.cedula
        '''
    cur.execute(sql)
 
    rows = cur.fetchall()

    for row in rows:
        propuesta = {
            'cedula': row[0],
            'apellidos': row[1],
            'nombres': row[2],
            'term':row[3],
            'propuesta':row[4],
            'estado': row[5]
        }
        lista['propuestas'].append(propuesta)
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

def crear_propuesta(propuesta):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()

    sql = "INSERT INTO api_propuesta(codigo,fecha_entrega,titulo,estatus,fk_term_id) VALUES ('{0}','{1}','{2}','{3}',{4})".format(propuesta['codigo'],propuesta['fecha_entrega'],propuesta['titulo'],propuesta['estatus'],propuesta['fk_term'])
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_propuesta WHERE titulo='{0}'".format(propuesta['titulo'])
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_propuesta = row[0]
    print(id_propuesta)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format(propuesta['estudiante_uno'])
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_estudiante_uno = row[0]
    print(id_estudiante_uno)

    sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_estudiante_uno)
    cur.execute(sql)
    conn.commit()

    if (not isEmpty(propuesta['estudiante_dos'])):
        sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format(propuesta['estudiante_dos'])
        cur.execute(sql)
        row = list(cur.fetchall()[0])
        id_estudiante_dos = row[0]
        print(id_estudiante_uno)

        sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_estudiante_dos)
        cur.execute(sql)
        conn.commit()

    if (not isEmpty(propuesta['tutor_academico'])):
        sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format(propuesta['tutor_academico'])
        cur.execute(sql)
        row = list(cur.fetchall()[0])
        id_tutor_academico = row[0]
        print(id_tutor_academico)

        sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_tutor_academico)
        cur.execute(sql)
        conn.commit()

    if (not isEmpty(propuesta['tutor_empresarial'])):
        sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format(propuesta['tutor_empresarial'])
        cur.execute(sql)
        row = list(cur.fetchall()[0])
        id_tutor_empresarial = row[0]
        print(id_tutor_empresarial)

        sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_tutor_empresarial)
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
