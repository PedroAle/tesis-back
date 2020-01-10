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
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('511821','Profesor','Mercedes','','Martinez','Rondon','mrondon@ucab.edu.ve','mercedesmr@gmail.com','m1234','04148903567','','','Gestor')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('14532372','Profesor','Liliana','Glenis','Martinez','Landazabul','lglenis@ucab.edu.ve','lilianag@gmail.com','lili456','04123456789','','','Gestor')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('6123724','Profesor','Ludwig','Antonio','Vera','Rojas','lvera@ucab.edu.ve','lrojas@gmail.com','la578','04160235879','','','Gestor')
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

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('23315675','Estudiante','Daniel','Alejandro','Asmat','Sanchez','daasmat@est.ucab.edu.ve','danielass@gmail.com','da543','0412543720','','','Invitado')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('20820139','Estudiante','Bassil','German','Dacostas','Frias','bgdacostas@est.ucab.edu.ve','germanfrias@gmail.com','df345','04242345675','','','Invitado')
    cur.execute(sql)
    conn.commit()

    sql = '''INSERT INTO 
            api_usuario(cedula,tipo,primer_nombre,segundo_nombre,primer_apellido,segundo_apellido,correo_ucab,correo_personal,password,telefono_uno,telefono_dos,observaciones,rol) 
            VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}','{10}','{11}','{12}')'''.format('21115533','Estudiante','Luis','Fernando','Contreras','Manzanilla','lfcontreras@est.ucab.edu.ve','luisfercontreras@gmail.com','lc456','04148923452','','','Invitado')
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

    sql = "INSERT INTO api_term(term) VALUES ('{}')".format('201454')
    cur.execute(sql)
    conn.commit()

    sql = "INSERT INTO api_term(term) VALUES ('{}')".format('201640')
    cur.execute(sql)
    conn.commit()

    sql = "INSERT INTO api_term(term) VALUES ('{}')".format('201431')
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

    sql = "INSERT INTO api_propuesta(codigo,fecha_entrega,titulo,estatus,fk_term_id) VALUES ('{0}','{1}','{2}','{3}',{4})".format('2357','2013-01-12','ALGORITMO GENÉTICO QUE RESUELVE EL PROBLEMA DE CORTES EN UNA DIMENSIÓN','Aprobada',id_term)
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

    sql = "INSERT INTO api_propuesta(codigo,fecha_entrega,titulo,estatus,fk_term_id) VALUES ('{0}','{1}','{2}','{3}',{4})".format('8985','2015-05-03','ANÁLISIS Y DISEÑO DE UN SISTEMA DE INFORMACIÓN PARA MRP','Aprobada',id_term)
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

    ######################################

    sql = "SELECT id FROM api_term WHERE term='{0}'".format('201454')    
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_term = row[0]
    print(id_term)

    sql = "INSERT INTO api_propuesta(codigo,fecha_entrega,titulo,estatus,fk_term_id) VALUES ('{0}','{1}','{2}','{3}',{4})".format('5467','2014-01-02','METODOLOGÍA PARA LA IMPLEMENTACIÓN DE UN SISTEMA ORIENTADO A LA AUTOMATIZACIÓN DE PROCESOS DE VENTA PARA INSTITUCIONES FINANCIERAS','Aprobada',id_term)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_propuesta WHERE titulo='{0}'".format('METODOLOGÍA PARA LA IMPLEMENTACIÓN DE UN SISTEMA ORIENTADO A LA AUTOMATIZACIÓN DE PROCESOS DE VENTA PARA INSTITUCIONES FINANCIERAS')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_propuesta = row[0]
    print(id_propuesta)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('23315675')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_estudiante_uno = row[0]
    print(id_estudiante_uno)

    sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_estudiante_uno)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('511821')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_tutor_academico = row[0]
    
    sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_tutor_academico)
    cur.execute(sql)
    conn.commit()

    ###################################

    sql = "SELECT id FROM api_term WHERE term='{0}'".format('201640')    
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_term = row[0]
    print(id_term)

    sql = "INSERT INTO api_propuesta(codigo,fecha_entrega,titulo,estatus,fk_term_id) VALUES ('{0}','{1}','{2}','{3}',{4})".format('2930','2016-03-12','ANÁLISIS, DISEÑO E IMPLEMENTACIÓN DE SOFTWARE PARA EL MANEJO DE LLAMADAS TELEFÓNICAS SOBRE REDES IP','Rechazada',id_term)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_propuesta WHERE titulo='{0}'".format('ANÁLISIS, DISEÑO E IMPLEMENTACIÓN DE SOFTWARE PARA EL MANEJO DE LLAMADAS TELEFÓNICAS SOBRE REDES IP')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_propuesta = row[0]
    print(id_propuesta)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('20820139')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_estudiante_uno = row[0]
    print(id_estudiante_uno)

    sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_estudiante_uno)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('14532372')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_tutor_academico = row[0]
    
    sql = "INSERT INTO api_usuariopropuesta(fk_propuesta_id,fk_usuario_id) VALUES ('{0}','{1}')".format(id_propuesta,id_tutor_academico)
    cur.execute(sql)
    conn.commit()

    #############################

    sql = "SELECT id FROM api_term WHERE term='{0}'".format('201431')    
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_term = row[0]
    print(id_term)

    sql = "INSERT INTO api_propuesta(codigo,fecha_entrega,titulo,estatus,fk_term_id) VALUES ('{0}','{1}','{2}','{3}',{4})".format('1095','2014-06-01','SISTEMA DE INFORMACIÓN CONTABLE ORIENTADO A LA PEQUEÑA Y MICROEMPRESA','Rechazada',id_term)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_propuesta WHERE titulo='{0}'".format('SISTEMA DE INFORMACIÓN CONTABLE ORIENTADO A LA PEQUEÑA Y MICROEMPRESA')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_propuesta = row[0]
    print(id_propuesta)

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('21115533')
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

    sql = "SELECT id FROM api_usuario WHERE cedula='{0}'".format('6123724')
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

    sql = "INSERT INTO api_trabajodegrado(codigo,titulo,nrc,descriptores,categoria,fecha_entrega,nombre_empresa,estatus,fk_propuesta_id,fk_term_id) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}',{8},{9})".format('TG6879','ALGORITMO GENÉTICO QUE RESUELVE EL PROBLEMA DE CORTES EN UNA DIMENSIÓN','25048','','Breve descripcion de  la tesis','12/06/2013','','Aprobada',id_propuesta,id_term)
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

    sql = "INSERT INTO api_trabajodegrado(codigo,titulo,nrc,descriptores,categoria,fecha_entrega,nombre_empresa,estatus,fk_propuesta_id,fk_term_id) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}',{8},{9})".format('TG4367','ANÁLISIS Y DISEÑO DE UN SISTEMA DE INFORMACIÓN PARA MRP','27650','','Breve descripcion de la tesis','03/11/2015','Cuadrado','Aprobada',id_propuesta,id_term)
    cur.execute(sql)
    conn.commit()

    sql = "SELECT id FROM api_propuesta WHERE titulo='{0}'".format('METODOLOGÍA PARA LA IMPLEMENTACIÓN DE UN SISTEMA ORIENTADO A LA AUTOMATIZACIÓN DE PROCESOS DE VENTA PARA INSTITUCIONES FINANCIERAS')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_propuesta = row[0]

    sql = "SELECT fk_term_id FROM api_propuesta WHERE titulo='{0}'".format('METODOLOGÍA PARA LA IMPLEMENTACIÓN DE UN SISTEMA ORIENTADO A LA AUTOMATIZACIÓN DE PROCESOS DE VENTA PARA INSTITUCIONES FINANCIERAS')
    cur.execute(sql)
    row = list(cur.fetchall()[0])
    id_term = row[0]

    sql = "INSERT INTO api_trabajodegrado(codigo,titulo,nrc,descriptores,categoria,fecha_entrega,nombre_empresa,estatus,fk_propuesta_id,fk_term_id) VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}',{8},{9})".format('TG7543','METODOLOGÍA PARA LA IMPLEMENTACIÓN DE UN SISTEMA ORIENTADO A LA AUTOMATIZACIÓN DE PROCESOS DE VENTA PARA INSTITUCIONES FINANCIERAS','24509','','Breve descripcion de la tesis','20/07/2014','','Rechazada',id_propuesta,id_term)
    cur.execute(sql)
    conn.commit()

    conn.close()

def insertar_defensa():
    conn = create_connection('db.sqlite3')
    cur = conn.cursor()

    sql = "SELECT id FROM api_trabajodegrado WHERE codigo='{0}'".format('TG6879')
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

    sql = "INSERT INTO api_defensa(codigo,fecha_hora,calificacion,mencion_publicacion,mencion_honorifica,nota,fk_trabajo_grado_id) VALUES ('{0}','{1}',{2},{3},{4},{5},{6})".format('D6879','2020-07-22 14:00:00',15,0,0,1,id_trabajodegrado)
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

    sql = "SELECT id FROM api_trabajodegrado WHERE codigo='{0}'".format('TG4367')
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

    #############

    sql = "SELECT id FROM api_trabajodegrado WHERE codigo='{0}'".format('TG4367')
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

    sql = "INSERT INTO api_defensa(codigo,fecha_hora,calificacion,mencion_publicacion,mencion_honorifica,nota,fk_trabajo_grado_id) VALUES ('{0}','{1}',{2},{3},{4},{5},{6})".format('D4367','2016-03-14 11:00:00',13,0,1,1,id_trabajodegrado)
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

    #############

    sql = "SELECT id FROM api_trabajodegrado WHERE codigo='{0}'".format('TG4367')
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

    sql = "INSERT INTO api_defensa(codigo,fecha_hora,calificacion,mencion_publicacion,mencion_honorifica,nota,fk_trabajo_grado_id) VALUES ('{0}','{1}',{2},{3},{4},{5},{6})".format('D4367','2016-03-14 11:00:00',15,0,1,1,id_trabajodegrado)
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

    #############

    sql = "SELECT id FROM api_trabajodegrado WHERE codigo='{0}'".format('TG4367')
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

    sql = "INSERT INTO api_defensa(codigo,fecha_hora,calificacion,mencion_publicacion,mencion_honorifica,nota,fk_trabajo_grado_id) VALUES ('{0}','{1}',{2},{3},{4},{5},{6})".format('D4367','2016-03-14 11:00:00',17,0,1,1,id_trabajodegrado)
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

    #############

    sql = "SELECT id FROM api_trabajodegrado WHERE codigo='{0}'".format('TG4367')
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

    sql = "INSERT INTO api_defensa(codigo,fecha_hora,calificacion,mencion_publicacion,mencion_honorifica,nota,fk_trabajo_grado_id) VALUES ('{0}','{1}',{2},{3},{4},{5},{6})".format('D4367','2015-12-04 11:00:00',17,0,1,1,id_trabajodegrado)
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
        