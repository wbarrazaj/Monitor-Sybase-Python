#from  ..class.Database import connect
from clases import Database
#import class.Database
from os import walk

#fh_servers=open("servidores.txt","r");
#for server in fh_servers:
   #fh_sentencias = open("senten 
#
sentenciasdir = "../datos/sentencias/healthcheck"

filenames = next(walk(sentenciasdir), (None, None, []))[2]
print(filenames)
