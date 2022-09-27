#from clases.Database import Database
from os import walk

outdir = "../salidas"
sentenciasdir = "../datos/sentencias/healthcheck"
filenames = next(walk(sentenciasdir), (None, None, []))[2]
fh_servers=open("../datos/servidores.txt","r");

#Limpia archivos de salida
for file in filenames:
  filespec = file.split(".")
  outfile=outdir+"/"+filespec[0]+".log"
  fh = open(outfile,"w")
  fh.close()
  print(outfile)

for server in fh_servers:
  print("============> "+server);
  for file in filenames:
    filespec = file.split(".")
    outfile=outdir+"/"+filespec[0]+".log"
    fh_sentencias = open(sentenciasdir+"/"+file, "r")
    sql=fh_sentencias.read() + "OUTPUT TO "+outfile
    print(sql)
    fh_sentencias.close()

fh_servers.close()


