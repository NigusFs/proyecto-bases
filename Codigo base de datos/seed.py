from configuraciones import *
import psycopg2
conn = psycopg2.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,passwd))
cur = conn.cursor()

sql ="""
  	INSERT INTO dentistas (rut,nombre,experiencia) 
  		VALUES (1000008,'Jon Snow',10);
  	INSERT INTO dentistas (rut,nombre,experiencia) 
  		VALUES (1252633,'Jamie Lannister',15);
  	INSERT INTO dentistas (rut,nombre,experiencia)
  		VALUES (15151454,'Mikasa Ackermann',7);
  	INSERT INTO dentistas (rut,nombre,experiencia)
  	VALUES (194251546,'Bruce Wayne',35);

  	INSERT INTO pacientes(rut,nombre,afiliacion) 	
  		VALUES (52255122,'Juan Perez','FONASA');
  	INSERT INTO pacientes(rut,nombre,afiliacion) 
  		VALUES (515515122,'Eren Jaeger','kyojin');
  	INSERT INTO pacientes(rut,nombre,afiliacion) 
  		VALUES (50225222,'Yondu','Ravagers');
  
"""
cur.execute(sql)

sql ="""
	INSERT INTO alergias (rut_paciente,nombre)
 		values (515515122,'Ibuprofeno');
	INSERT INTO alergias (rut_paciente,nombre)
 		values (52255122,'Sin alergias');
	INSERT INTO alergias (rut_paciente,nombre)
 		values (50225222,'Paracetamol');

"""
cur.execute(sql)

sql ="""
  	INSERT INTO proveedores (nombre,precio_envio,tiempo_envio)
  		VALUES ('Guardianes de la Noche',15000,3);
	INSERT INTO proveedores (nombre, precio_envio,tiempo_envio)
		VALUES ('Defenders',1000,2);

	INSERT INTO productos(nombre,stock,marca,nombre_proveedor)
		VALUES ('anestecia',20,'adidas','Defenders');
	INSERT INTO productos(nombre,stock,marca,nombre_proveedor) 
		VALUES ('anestecia',30,'adidas','Guardianes de la Noche');	
"""
cur.execute(sql)


sql="""
	INSERT INTO proveedores_productos(proveedor_id,producto_id)
		VALUES (2,1);
	INSERT INTO proveedores_productos(proveedor_id,producto_id)
		VALUES (1,2);
"""
cur.execute(sql)

sql ="""
	INSERT INTO tratamientos (nombre,dificultad)
		values ('Limpieza',2),('Extraccion molares',6);
"""
cur.execute(sql)

sql="""
	INSERT INTO disponibilidad_dentista(nombre,rut_dentista,fecha,hora)
		VALUES ('Jon Snow',1000008,'2017-06-16',1000);	

	INSERT INTO disponibilidad_dentista(nombre,rut_dentista,fecha,hora)
		VALUES ('Mikasa Ackermann',15151454,'2017-06-16',1030);
	INSERT INTO disponibilidad_dentista(nombre,rut_dentista,fecha,hora)
		VALUES ('Mikasa Ackermann',15151454,'2017-06-16',1230);	

	INSERT INTO disponibilidad_dentista(nombre,rut_dentista,fecha,hora)
		VALUES ('Jamie Lannister',1252633,'2017-06-16',0800);
	INSERT INTO disponibilidad_dentista(nombre,rut_dentista,fecha,hora)
		VALUES ('Jamie Lannister',1252633,'2017-06-16',0900);
	INSERT INTO disponibilidad_dentista(nombre,rut_dentista,fecha,hora)
		VALUES ('Jamie Lannister',1252633,'2017-06-16',1230);

	INSERT INTO disponibilidad_dentista(nombre,rut_dentista,fecha,hora)
		VALUES ('Jon Snow',1000008,'2017-06-17',1000);
	insert into disponibilidad_dentista (nombre,rut_dentista,fecha,hora) 
		values ('Jon Snow',1000008,'2017-06-17',1400);
		

"""
cur.execute(sql)

sql="""
	INSERT INTO reservas (hora,fecha,tratamiento_nombre) 
		VALUES (1000,'2017-06-16','Limpieza');
	INSERT INTO reservas (hora,fecha,tratamiento_nombre) 
		VALUES (1030,'2017-06-16','Extraccion molares');
	INSERT INTO pacientes_reservas(rut_paciente,reserva_id)
		VALUES (50225222,1);
	INSERT INTO pacientes_reservas(rut_paciente,reserva_id)
		VALUES (515515122,2);

	INSERT INTO dentistas_reservas(rut_dentista,reserva_id)
		VALUES (1000008,1);
	INSERT INTO dentistas_reservas(rut_dentista,reserva_id)
		VALUES (15151454,2);
	DELETE FROM disponibilidad_dentista
		WHERE rut_dentista=1000008 AND fecha='2017-06-16' AND hora= 1000;
	DELETE FROM disponibilidad_dentista
		WHERE rut_dentista=15151454 AND fecha='2017-06-16' AND hora= 1030;
"""
cur.execute(sql)
# TABLA NO NECESARIA
#sql="""
#	INSERT INTO tratamiento_dentista(tratamiento_id,rut_dentista)
#		VALUES (7,1000008);
#	INSERT INTO tratamiento_dentista(tratamiento_id,rut_dentista)
#		VALUES (8,15151454);
#"""
#cur.execute(sql)

## asociar los productos a los tratamientos con un script
##if tratamiento.nombre==extaccion molares then tratamiento.id <=> producto.id where producto.nombre == 'anestecia'
sql="""
	INSERT INTO tratamientos_productos(tratamiento_id,producto_id)
		VALUES (2,1),(2,2);
	
"""
cur.execute(sql)


#asociar tramientos a reservas automaticamente usar un script
sql="""
	INSERT INTO tratamientos_reservas(tratamiento_id,reserva_id)
		VALUES (1,1),(2,2);
	
"""
cur.execute(sql)












#preguntar si esta bien !!
#sql ="""
#insert INTO tratamiento_producto (tratamiento_id,producto_id) 	(SELECT id,%i  FROM tratamiento where nombre = 'Limpieza' or 
## nombre = 'Extraccion molares'
#);"""%(producto_id)

#cur.execute(sql)

#sql ="""
#insert INTO proveedor_producto (proveedor_id,producto_id) 
#	(SELECT id,%i  FROM proveedor where nombre = 'Guardiannes de la noche'
#);"""%(producto_id)

#cur.execute(sql)

#sql ="""insert INTO usuarios (nombre,apellido,email,passwd,creado)
# values ('Manuel','Alba','malba@mmae.cl','1234',now() );
#"""
#cur.execute(sql)

#post_id = cur.fetchone()[0]

#print post_id

## esto mete los datos en las tablas relacionales 
#sql ="""insert INTO tratamientos_dentista (tratamiento_id,rut_dentistas)
#(SELECT id,%i  FROM categorias where nombre = 'Cine' or 
# nombre = 'Geek' or 
 # nombre = 'Mundo Marvel'
#);"""%(post_id)


conn.commit()
cur.close()
conn.close()
