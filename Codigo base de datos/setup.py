#from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname='bases' user='postgres' host='localhost' password='1122334455'")

cur = conn.cursor()
sql ="""select 'drop table "' || tablename || '" cascade;' from pg_tables;"""

cur.execute(sql)
#cambiar rut a varchar para colocar la k o.o  
sql ="""
CREATE TABLE dentistas
           (rut integer PRIMARY KEY not null , nombre varchar(100),experiencia integer);

CREATE TABLE tratamientos
			(tratamiento_id serial PRIMARY KEY not null, nombre varchar(100),dificultad integer );

CREATE TABLE productos
			(producto_id serial PRIMARY KEY not null, nombre varchar(100),stock integer,marca varchar (50),nombre_proveedor varchar(100));

CREATE TABLE proveedores
			(proveedor_id serial PRIMARY KEY not null, nombre varchar(100),precio_envio integer,tiempo_envio float);

CREATE TABLE reservas
			(reserva_id serial PRIMARY KEY not null, hora integer , fecha date,tratamiento_nombre varchar(100));

CREATE TABLE pacientes
           (rut integer PRIMARY KEY not null , nombre varchar(100),afiliacion varchar(50));

CREATE TABLE alergias
           (rut_paciente integer,nombre varchar(100));
CREATE TABLE disponibilidad_dentista
           (nombre varchar(100),rut_dentista integer,fecha date, hora integer);


CREATE TABLE tratamientos_productos
           (tratamiento_id integer,producto_id integer);            
CREATE TABLE proveedores_productos
           (proveedor_id integer,producto_id integer);
CREATE TABLE tratamientos_reservas
           (tratamiento_id integer,reserva_id integer);
CREATE TABLE pacientes_reservas
           (rut_paciente integer,reserva_id integer);
CREATE TABLE dentistas_reservas
           (rut_dentista integer,reserva_id integer);
"""



#cur.execute(sql)
#conn.commit()

#sql = """

  
 # INSERT INTO dentistas (rut,nombre,experiencia) VALUES (1000008,'Jon Snow',10);
 # INSERT INTO dentistas (rut,nombre,experiencia) VALUES (1252633,'Jamie Lannister',15);
 # INSERT INTO dentistas (rut,nombre,experiencia) VALUES (15151454,'Mikasa Ackermann',7);
 # INSERT INTO pacientes(rut,nombre,afiliacion) VALUES (52255122,'Juan Perez','FONASA');
 # INSERT INTO pacientes(rut,nombre,afiliacion) VALUES (515515122,'Eren Jaeger','kyojin');
 # INSERT INTO pacientes(rut,nombre,afiliacion) VALUES (50225222,'Yondu','Ravagers');
 # INSERT INTO productos (productos_id,nombre,stock,marca) VALUES (,anestecia,100,bauer);
 # INSERT INTO tratamientos (tratamientos_id,nombre,dificultad)  VALUES (,molares,4);
 # INSERT INTO proveedores (proveedor_id,nombre,precio_envio,tiempo_envio) #VALUES (,Guardianes de la Noche,15000,3);
#  INSERT INTO reservas (reserva_id,hora,dia) VALUES (,1000,'2017-06-16');
#"""

cur.execute(sql)
conn.commit()

cur.close()
conn.close()
