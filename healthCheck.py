import pyodbc
import pymysql
#from clases.Database import Database
from clases.cls_Bdd import BaseDD
from os import walk
from pathlib import Path
import sys
import os
from datetime import datetime
import shutil


def error(texto):
  sys.exit(texto)

#Validar parámetros recibidos
cantidad = len(sys.argv)
if cantidad ==1:
  error("Debe indicar el archivo de conexiones de bdd.")

if cantidad > 2:
  error("Demasiados parametros")

#Valida que exista el archivo de conexiones
archivoConexiones = sys.argv[1]
path = Path(archivoConexiones)
if not path.is_file():
  error("Archivo de conexiones ("+archivoConexiones+") no existe")

fh_conexiones=open(archivoConexiones)
prefijo = datetime.timestamp(datetime.now())
print(prefijo)


outdir = "/tmp/healthcheck_"+ str(prefijo)
print (outdir)
os.mkdir(os.path.join("/tmp", "healthcheck_"+str(prefijo)))
os.chmod(outdir,0o0777)
sentenciasdir = "datos/sentencias/healthcheck"

"""
#Limpia archivos de salida
for file in archivosSql:
  filespec = file.split(".")
  outfile=outdir+"/"+filespec[0]+".log"
  fh = open(outfile,"w")
  fh.close()
  print(outfile)
"""

for conn in fh_conexiones:
  print("============> "+conn);
  # [0] tipo de bdd, [1] nombre/IP, [2] usuario, [3] clave, [4] bdd. [5] puerto
  lineaConn = conn.split(",")
  tipoBdd = lineaConn[0]
  bdd = lineaConn[4]

  dbConn=BaseDD(servidor=lineaConn[1], usuario=lineaConn[2], clave=lineaConn[3], db=lineaConn[4], puerto=lineaConn[5], drver='', motor='MariaDB')
  print(sentenciasdir+"/"+tipoBdd)
  archivosSql = next(walk(sentenciasdir+"/"+tipoBdd), (None, None, []))[2]
  for file in archivosSql:
    filespec = file.split(".")
    outfile=outdir+"/"+filespec[0]+".log"
    fh_sentencias = open(sentenciasdir+"/"+tipoBdd+"/"+file, "r")
    #sql=fh_sentencias.read() + "INTO OUTFILE '"+outfile+"'"
    sql=fh_sentencias.read()+";"
    sql=sql.replace("#SPOOLFILE#", outfile)
    fh_sentencias.close()
    #dbConn.ejecutar_query(sql)
    sql="select 'hola',1,2,100 INTO OUTFILE '"+outfile+"';"
    print(sql)
    dbConn.ejecutar_query("select 'hola',1,2,100 INTO OUTFILE '"+outfile+"';")

fh_conexiones.close()

shutil.move(outdir,"./salidas")



