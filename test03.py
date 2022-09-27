from clases.cls_Bdd import BaseDD

database=BaseDD(servidor='Ares2', usuario='root',clave='Emilita01',db='Prueba',puerto='3306',drver='', motor='MariaDB')
print(database)
database.ejecutar_query("select 'Hola'")

