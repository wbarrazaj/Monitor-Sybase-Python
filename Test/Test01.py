import sqlanydb
import os

#print(os.environ["SQLANY_API_DLL"])


conn = sqlanydb.connect(uid='sa', pwd='Emilita01', eng='PROD' , commlinks='tcpip{host=193.168.1.175;port=5000}' )
curs = conn.cursor()
curs.execute("select 'Hello, world!'")
print( "SQL Anywhere says: %s" % curs.fetchone() )
curs.close()
conn.close()



def print_(mensaje):
    print(mensaje)
    print("Hola")


print_("Chao")


class Jorge() :
    XX = 1
    YY = 2 
    def Gauchon():
        pass

jomito = Jorge()

print(jomito.XX)

