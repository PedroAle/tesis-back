
from api.models import Term
from sqlite3 import Error
from api.services.connection import create_connection
import sqlite3
from api.services.utils import isEmpty, generateError, successAction, isNumber 
import json

def obtener_trabajosdegrado():
    lista = {'trabajosdegrado':[]}
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    cur.execute("SELECT * FROM api_trabajodegrado")
 
    rows = cur.fetchall()

    for row in rows:
        trabajodegrado = {
            'id': row[0],
            'codigo': row[1],
            'titulo': row[2],
            'nrc': row[3],
            'descriptores': row[4],
            'categoria': row[5],
            'fecha_entrega':row[6],
            'nombre_empresa': row[7],
            'estatus':row[8],
            'fk_propuesta': row[9],
            'fk_term': row[10]
        }
        lista['trabajosdegrado'].append(trabajodegrado)
    return lista

def obtener_trabajodegrado(id):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "SELECT * FROM api_trabajodegrado WHERE id={0}".format(id)
    cur.execute(sql)
 
    row = cur.fetchall()
    trabajodeg = list(row[0])
    print(trabajodeg)

    sql = "SELECT term FROM api_term WHERE id={0}".format(trabajodeg[10])
    cur.execute(sql)
    row = cur.fetchall()
    term = list(row[0])
    print(term)

    trabajodegrado = {
        'id': trabajodeg[0],
        'codigo': trabajodeg[1],
        'titulo':trabajodeg[2],
        'nrc': trabajodeg[3],
        'descriptores': trabajodeg[4],
        'categoria': trabajodeg[5],
        'fecha_entrega':trabajodeg[6],
        'nombre_empresa': trabajodeg[7],
        'estatus':trabajodeg[8],
        'fk_propuesta': trabajodeg[9],
        'fk_term': term[0]
    }
    return trabajodegrado

def crear_trabajodegrado(trabajodegrado):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()

    sql = "INSERT INTO api_trabajodegrado(codigo,titulo,nrc,descriptores,categoria,fecha_entrega,nombre_empresa,estatus,fk_propuesta_id,fk_term_id) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}',{8},{9})".format(trabajodegrado['codigo'],trabajodegrado['titulo'],trabajodegrado['nrc'],trabajodegrado['descriptores'],trabajodegrado['categoria'],trabajodegrado['fecha_entrega'],trabajodegrado['nombre_empresa'],trabajodegrado['estatus'],trabajodegrado['fk_propuesta'],trabajodegrado['fk_term'])
    cur.execute(sql)
    conn.commit()

def actualizar_trabajodegrado(trabajodegrado):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = '''UPDATE api_trabajodegrado 
            SET codigo='{0}', titulo='{1}', nrc='{2}', descriptores='{3}', categoria='{4}', fecha_entrega='{5}', nombre_empresa='{6}', estatus='{7}'
            WHERE id={8}'''.format(trabajodegrado['codigo'],trabajodegrado['titulo'],trabajodegrado['nrc'],trabajodegrado['descriptores'],trabajodegrado['categoria'],trabajodegrado['fecha_entrega'],trabajodegrado['nombre_empresa'],trabajodegrado['estatus'],trabajodegrado['id'])
    cur.execute(sql)
    conn.commit()

def eliminar_trabajodegrado(id):
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "DELETE FROM api_trabajodegrado WHERE id={0}".format(id)
    cur.execute(sql)
    conn.commit()
