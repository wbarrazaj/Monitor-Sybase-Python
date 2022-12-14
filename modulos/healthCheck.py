#from clases.Database import Database
from ..clases.cls_Bdd import BaseDD
from os import walk
from pathlib import Path
import sys



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


outdir = "../salidas"
sentenciasdir = "../datos/sentencias/healthcheck"

#Limpia archivos de salida
for file in archivosSql:
  filespec = file.split(".")
  outfile=outdir+"/"+filespec[0]+".log"
  fh = open(outfile,"w")
  fh.close()
  print(outfile)

for server in fh_conexiones:
  print("============> "+server);
  # [0] tipo de bdd, [1] nombre/IP, [2] usuario, [3] clave, [4] bdd. [5] puerto
  lineaConn = file.split(",")
  tipoBdd = lineaConn[0]
  bdd = lineaConn[4]
  archivosSql = next(walk(sentenciasdir+"/"+bdd), (None, None, []))[2]
  for file in archivosSql:
    filespec = file.split(".")
    outfile=outdir+"/"+filespec[0]+".log"
    fh_sentencias = open(sentenciasdir+"/"+file, "r")
    sql=fh_sentencias.read() + "OUTPUT TO "+outfile
    print(sql)
    fh_sentencias.close()

fh_conexiones.close()


