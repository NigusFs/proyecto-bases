#from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname='bases' user='postgres' host='localhost' password='1122334455'")

cur = conn.cursor()
sql ="""select 'drop table "' || tablename || '" cascade;' from pg_tables;"""

cur.execute(sql)

sql ="""
DROP TABLE alergias;
DROP TABLE dentistas;
DROP TABLE dentistas_reservas;
DROP TABLE disponibilidad_dentista;
DROP TABLE pacientes;
DROP TABLE pacientes_reservas;
DROP TABLE productos;
DROP TABLE proveedores;
DROP TABLE proveedores_productos;
DROP TABLE reservas;
DROP TABLE tratamientos_productos;
DROP TABLE tratamientos;
DROP TABLE tratamientos_reservas;
"""



cur.execute(sql)
conn.commit()

cur.close()
conn.close()
