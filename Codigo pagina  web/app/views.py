from app import app
from flask import render_template, request, redirect
from configuraciones import *

import psycopg2
conn = psycopg2.connect("dbname=%s user=%s host=%s password=%s"%(database,user,host,passwd))
cur = conn.cursor()

@app.route('/')

@app.route('/index')
def index():
    sql="""
    select dentistas.nombre,count(*)as sesiones_disponibles from 
    disponibilidad_dentista,dentistas where 
    dentistas.rut=rut_dentista 
    group by dentistas.nombre order by sesiones_disponibles desc;
    """
    #print(sql)
    cur.execute(sql)
    hora = cur.fetchall()

    sql="""
    select * from disponibilidad_dentista where
    nombre='Jamie Lannister' ;
    """
    cur.execute(sql)
    dentistaJ = cur.fetchall()

    sql="""
    select * from disponibilidad_dentista where
    nombre='Mikasa Ackermann' ;
    """
    cur.execute(sql)
    dentistaM = cur.fetchall()

    sql="""
    select * from disponibilidad_dentista where
    nombre='Jon Snow' ;
    """
    cur.execute(sql)
    dentistaS = cur.fetchall()

    sql="""
    select nombre,experiencia from dentistas order by experiencia desc ;
    """
    cur.execute(sql)
    dentistas = cur.fetchall()

    sql="""
    select nombre,proveedor_id from proveedores;
    """

    cur.execute(sql)
    proveedores = cur.fetchall()


    return render_template("index.html",hora=hora,dentistas=dentistas,dentisaJ=dentistaJ,dentistaS=dentistaS,dentistaM=dentistaM,proveedores=proveedores)


@app.route('/indexform')
def indexform():
    #conn = psycopg2.connect("dbname='bases' user='postgres' host='localhost' password='1122334455'")
    #cur = conn.cursor()
    sql="""
    select dentistas.nombre,count(*)as sesiones_disponibles from 
    disponibilidad_dentista,dentistas where 
    dentistas.rut=rut_dentista 
    group by dentistas.nombre;
    """
    print(sql)
    cur.execute(sql)
    hora = cur.fetchall()

    return render_template("index-form.html", hora=hora)


@app.route('/indexvideo')
def indexvideo():
    return render_template("index-video.html")
