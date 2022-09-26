import pyodbc 

class Conexion():
    """
    Server class de Conexion.
    __conectar    : metodo de conexion.
    """
    def __init__(self, servidor, usuario, clave, db, puerto, drver ):
        self.ServidorDB = servidor 
        self.UsuarioDB =  usuario
        self.PasswordDB = clave
        self.SchemaDBD = db
        self.Port = puerto 
        self.Driver = drver
    
    def conectar(self):
        conn = pyodbc.connect(
                                driver=self.Driver, 
                                server=self.ServidorDB , 
                                database=self.SchemaDBD ,
                                port = self.Port,
                                uid=self.UsuarioDB, 
                                pwd=self.PasswordDB
                              )
        return conn

    def ejecutar_query(self, query):
        conn=self.__conectar()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

    def chk_default(c):
        res = True
        try:
            c.query('select 1')
            c.use_result()
        except:
            res = False
            
        return res


""""
serv = "Server_name"
usr = "Username" 
passwd = "Password"
db = "database_name"
prt = "port"
drver="Adaptive Server Enterprise"
#driver="FreeTDS"
query="select count (*) from emp"
print (datetime.datetime.now())
conn = pyodbc.connect(driver=drver, server=serv, database=db,port = prt,uid=usr, pwd=passwd)
print(conn)
cursor = conn.cursor()
cursor.execute(query)
row = cursor.fetchall()
"""