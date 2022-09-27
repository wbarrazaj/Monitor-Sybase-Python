import sqlanydb


class Database:
  def __init__(self, uid, passwd, engine, server, port, protocol='tcpip' ):
    self.uid = uid
    self.passwd = passwd
    self.engine = engine
    self.server = server
    self.port = port
    self.protocol = protocol
    self.serverconn = protocol +'{host='+server+';port='+port+'}'

  def connect(self):
    self.conn = sqlanydb.connect(uid=self.uid, pwd=self.passwd, eng=self.engine , commlinks=self.server )
    return conn


  def close(self):
    self.conn.close()


kk = Database('sa', 'Emilita01', 'PROD', '193.168.1.175', '5000')

con= kk.connect()
con.close()
kk.close()
