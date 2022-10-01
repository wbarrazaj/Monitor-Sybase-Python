import pyodbc
import pymysql
from clases.cls_Bdd import BaseDD
from os import walk
from pathlib import Path
import sys
import os
from datetime import datetime
import shutil
import subprocess


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
sufijo = datetime.timestamp(datetime.now())
dirProceso = "healthcheck_"+ str(sufijo)


outdir = "/tmp/"+ dirProceso
print ("directorio de salida: "+outdir)

os.mkdir(os.path.join("/tmp", dirProceso))
os.chmod(outdir,0o0777)
os.mkdir(os.path.join("salidas", dirProceso))
sentenciasdir = "datos/sentencias/healthcheck"

#Crear archivo notAlive.log para los servicios que estén abajo
fh_alive = open("./salidas/"+ dirProceso +"/notAlive.log","w")

for conn in fh_conexiones:
  # [0] tipo de bdd, [1] nombre/IP, [2] usuario, [3] clave, [4] bdd. [5] puerto
  lineaConn = conn.split(",")
  print("=> base de datos: "+lineaConn[4]+"@"+lineaConn[1]+" ["+lineaConn[0]+"]");
  tipoBdd = lineaConn[0]
  bdd = lineaConn[4]

  dbConn=BaseDD(servidor=lineaConn[1], usuario=lineaConn[2], clave=lineaConn[3], db=lineaConn[4], puerto=lineaConn[5], drver='', motor='MariaDB')
  #print(sentenciasdir+"/"+tipoBdd)
  archivosSql = next(walk(sentenciasdir+"/"+tipoBdd), (None, None, []))[2]
  for file in archivosSql:
    print("   - "+file)
    filespec = file.split(".")
    outfile=outdir+"/"+filespec[0]+".log"
    fh_sentencias = open(sentenciasdir+"/"+tipoBdd+"/"+file, "r")
    #sql=fh_sentencias.read() + "INTO OUTFILE '"+outfile+"'"
    sql=fh_sentencias.read()+";"
    sql=sql.replace("#SERVER#", lineaConn[1])
    sql=sql.replace("#BD#", lineaConn[4])
    sql=sql.replace("#SPOOLFILE#", outfile)
    fh_sentencias.close()
    #print(sql)
    #try:
    dbConn.ejecutar_query(sql)
    #except Exception as e:
      #errorTxt = ""+e.__class__.__name__
      #if errorTxt.find("OperationalError") >= 0:
        #if filespec[0]=="espacio":
          #fh_alive.write(lineaConn[1]+","+lineaConn[4]+",0\n")
    #else:
      #print("Oops!", e.__class__, "occurred.")

    cmd = "cat "+outfile+" >> salidas/"+dirProceso+"/"+filespec[0]+".log"
    print(cmd)
    subprocess.run(cmd, shell=True)

fh_conexiones.close()
fh_alive.close()

try:
  shutil.move(outdir + "/*","salidas/"+dirProceso)
except Exception as e:
  print(".")



