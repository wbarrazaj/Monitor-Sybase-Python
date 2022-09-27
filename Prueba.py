#import sqlanydb
import os
import pyodbc

from clases.cls_Bdd import BaseDD

os.environ["SQLANY_API_DLL"]='/opt/sqlanywhere17/lib64/libdbcapi_r.so'

servidor='193.168.1.175:5000'
usuario='sa' 
clave='Emilita01'
db='master' 
puerto=5000
drver='SYBASE'

Conn = BaseDD(servidor,usuario,clave,db,puerto,drver)


print(Conn.ServidorDB)
a=pyodbc.drivers()

print(a)
print(Conn)

conn = pyodbc.connect(driver=drver, server=servidor , database=db ,uid=usuario , pwd=clave)

print("Aqui")

b=conn.conectar()

print(b)
print("Termino")