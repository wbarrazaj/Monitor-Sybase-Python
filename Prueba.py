#import sqlanydb
import os

from clases.Clase_Conexion import Conexion

os.environ["SQLANY_API_DLL"]='./opt/sqlanywhere17/lib64/libdbcapi_r.so'

servidor='193.168.1.175'
usuario='sa' 
clave='Emilita01'
db='master' 
puerto=5000
drver='Hola'

Conn = Conexion(servidor,usuario,clave,db,puerto,drver)


print(Conn.ServidorDB)

a=Conn.__conectar()

print(a)