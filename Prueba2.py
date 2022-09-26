import sqlanydb
import os

#print(os.environ["SQLANY_API_DLL"])

os.environ["SQLANY_API_DLL"]='/opt/sqlanywhere17/lib64/libdbcapi_r.so'
conn = sqlanydb.connect(uid='sa', pwd='Emilita01', dbn='master' , commlinks='tcpip{host=193.168.1.175;port=5000}' )
curs = conn.cursor()
curs.execute("select 'Hello, world!'")
print( "SQL Anywhere says: %s" % curs.fetchone() )
curs.close()
conn.close()
