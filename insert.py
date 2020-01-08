from sqlite3 import Error
from api.services.connection import create_connection
from api.services.utils import isEmpty
import sqlite3
import json

def insertar_usuarios():
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('8634590','Profesor','Beatriz','Alicia','Melo','Zerpa','mzerpa@ucab.edu.ve','beatrizerpa@gmail.com','b1234','04143567890','','','Administrador')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('4582205','Profesor','Raul','Arnold','Bustamante','Coello','rcoello@ucab.edu.ve','raulabustamante@gmail.com','r456','04126789345','','','Gestor')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('6234543','Profesor','Veronika','Fanny','Mendoza','Frisch','vmendoza@ucab.edu.ve','vfannym@gmail.com','v789','04165879023','','','Gestor')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('13552794','Externo','Danny','Yoxelin','Moreno','Rodriguez','','yoxelinmr@gmail.com','y928','04245648352','','','Invitado')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('16381631','Externo','Jose','Manuel','Morgado','Bello','','josemmbello@gmail.com','jm467','04247638234','','','Invitado')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('25342183','Estudiante','Andres','Enrique','Pirela','Loyo','apireal@est.ucab.edu.ve','andrespirela@gmail.com','ap784','04142356783','','','Invitado')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('24991544','Estudiante','Gabriel','Alfonso','Ariza','Suarez','gariza@est.ucab.edu.ve','gabrielasuarez@gmail.com','gaa371','04127648745','','','Invitado')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('26922495','Estudiante','Helen','Alejandra','Dias','Ferreira','hdias@est.ucab.edu.ve','alejandraferreira@gmail.com','hd238','04167349283','','','Invitado')
    cur.execute(sql)
    conn.commit()

    conn.close()

def insertar_term():
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()
    sql = "INSERT INTO api_term(term) VALUES ('{}')".format('201540')
    cur.execute(sql)
    conn.commit()

    sql = "INSERT INTO api_term(term) VALUES ('{}')".format('201343')
    cur.execute(sql)
    conn.commit()

    conn.close()

def insertar_propuesta():
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()

    sql = "SELECT id FROM api_term WHERE term='{0}'".format('201343')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_term = row[0]
    print(id_term)

    sql = "INSERT INTO api_propuesta(codigo,fecha_entrega,titulo,estatus,fk_term_id) VALUES ('{0}','{1}','{2}','{3}',{4})".format('2357','12/01/2013','ALGORITMO GENÉTICO QUE RESUELVE EL PROBLEMA DE CORTES EN UNA DIMENSIÓN','Aprobada',id_term)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_propuesta WHERE titulo='{0}'".format('ALGORITMO GENÉTICO QUE RESUELVE EL PROBLEMA DE CORTES EN UNA DIMENSIÓN')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_propuesta = row[0]
    print(id_propuesta)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('25342183')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_estudiante_uno = row[0]
    print(id_estudiante_uno)

    sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_estudiante_uno)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('8634590')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_tutor_academico = row[0]
    
    sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_tutor_academico)
    cur.execute(sql)
    conn.commit()

    ###############

    sql = "SELECT id FROM api_term WHERE term='{0}'".format('201540')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_term = row[0]
    print(id_term)

    sql = "INSERT INTO api_propuesta(codigo,fecha_entrega,titulo,estatus,fk_term_id) VALUES ('{0}','{1}','{2}','{3}',{4})".format('8985','03/05/2015','ANÁLISIS Y DISEÑO DE UN SISTEMA DE INFORMACIÓN PARA MRP','Aprobada',id_term)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_propuesta WHERE titulo='{0}'".format('ANÁLISIS Y DISEÑO DE UN SISTEMA DE INFORMACIÓN PARA MRP')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_propuesta = row[0]
    print(id_propuesta)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('24991544')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_estudiante_uno = row[0]
    print(id_estudiante_uno)

    sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_estudiante_uno)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('26922495')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_estudiante_dos = row[0]
    
    sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_estudiante_dos)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('4582205')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_tutor_academico = row[0]
    
    sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_tutor_academico)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('13552794')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_tutor_empresarial = row[0]
    
    sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_tutor_empresarial)
    cur.execute(sql)
    conn.commit()

    conn.close()

def insertar_trabajodegrado():
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()

    sql = "SELECT id FROM api_propuesta WHERE titulo='{0}'".format('ALGORITMO GENÉTICO QUE RESUELVE EL PROBLEMA DE CORTES EN UNA DIMENSIÓN')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_propuesta = row[0]

    sql = "SELECT fk_term_id FROM api_propuesta WHERE titulo='{0}'".format('ALGORITMO GENÉTICO QUE RESUELVE EL PROBLEMA DE CORTES EN UNA DIMENSIÓN')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_term = row[0]

    sql = "INSERT INTO api_trabajodegrado(codigo,titulo,nrc,descriptores,categoria,fecha_entrega,nombre_empresa,estatus,fk_propuesta_id,fk_term_id) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}',{8},{9})".format('6879','ALGORITMO GENÉTICO QUE RESUELVE EL PROBLEMA DE CORTES EN UNA DIMENSIÓN','25048','','Breve descripcion de  la tesis','12/06/2013','','Aprobada',id_propuesta,id_term)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_propuesta WHERE titulo='{0}'".format('ANÁLISIS Y DISEÑO DE UN SISTEMA DE INFORMACIÓN PARA MRP')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_propuesta = row[0]

    sql = "SELECT fk_term_id FROM api_propuesta WHERE titulo='{0}'".format('ANÁLISIS Y DISEÑO DE UN SISTEMA DE INFORMACIÓN PARA MRP')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_term = row[0]

    sql = "INSERT INTO api_trabajodegrado(codigo,titulo,nrc,descriptores,categoria,fecha_entrega,nombre_empresa,estatus,fk_propuesta_id,fk_term_id) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}',{8},{9})".format('4367','ANÁLISIS Y DISEÑO DE UN SISTEMA DE INFORMACIÓN PARA MRP','27650','','Breve descripcion de la tesis','03/11/2015','Cuadrado','Aprobada',id_propuesta,id_term)
    cur.execute(sql)
    conn.commit()

    conn.close()

def insertar_defensa():
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()

    sql = "SELECT id FROM api_trabajodegrado WHERE codigo='{0}'".format('6879')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_trabajodegrado = row[0]
    print(id_trabajodegrado)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('8634590')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_jurado_uno = row[0]
    print(id_jurado_uno)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('4582205')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_jurado_dos = row[0]
    print(id_jurado_dos)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('6234543')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_jurado_tres = row[0]
    print(id_jurado_tres)

    sql = "INSERT INTO api_defensa(codigo,fecha_hora,calificacion,mencion_publicacion,mencion_honorifica,nota,fk_trabajo_grado_id) VALUES ('{0}','{1}',{2},{3},{4},{5},{6})".format('D6879','2013-11-22 14:00:00',15,0,0,1,id_trabajodegrado)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_defensa WHERE codigo='{0}'".format('D6879')
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

    #############

    sql = "SELECT id FROM api_trabajodegrado WHERE codigo='{0}'".format('4367')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_trabajodegrado = row[0]
    print(id_trabajodegrado)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('6234543')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_jurado_uno = row[0]
    print(id_jurado_uno)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('4582205')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_jurado_dos = row[0]
    print(id_jurado_dos)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('8634590')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_jurado_tres = row[0]
    print(id_jurado_tres)

    sql = "INSERT INTO api_defensa(codigo,fecha_hora,calificacion,mencion_publicacion,mencion_honorifica,nota,fk_trabajo_grado_id) VALUES ('{0}','{1}',{2},{3},{4},{5},{6})".format('D4367','2016-03-14 11:00:00',19.6,0,1,1,id_trabajodegrado)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_defensa WHERE codigo='{0}'".format('D4367')
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

    conn.close()

insertar_usuarios()
insertar_term()
insertar_propuesta()
insertar_trabajodegrado()
insertar_defensa()
        