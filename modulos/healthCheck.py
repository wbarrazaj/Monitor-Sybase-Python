#from clases.Database import Database
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


outdir = "../salidas"
sentenciasdir = "../datos/sentencias/healthcheck"
filenames = next(walk(sentenciasdir), (None, None, []))[2]
fh_conexiones=open("../datos/servidores.txt","r");

#Limpia archivos de salida
for file in filenames:
  filespec = file.split(".")
  outfile=outdir+"/"+filespec[0]+".log"
  fh = open(outfile,"w")
  fh.close()
  print(outfile)

for server in fh_conexiones:
  print("============> "+server);
  for file in filenames:
    filespec = file.split(".")
    outfile=outdir+"/"+filespec[0]+".log"
    fh_sentencias = open(sentenciasdir+"/"+file, "r")
    sql=fh_sentencias.read() + "OUTPUT TO "+outfile
    print(sql)
    fh_sentencias.close()

fh_conexiones.close()


