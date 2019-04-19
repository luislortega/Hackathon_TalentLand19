import psycopg2
import json

class ConexionDB:
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname='grupomodelo' user='postgres' host='localhost' password='1298Luis'")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            print("[✔] Base de datos conectada")
        except:
            print("[x] Error en la conexion")

    def crear_tablas_postgres(self):
        create_table_command = "CREATE TABLE entidad_federativa(id serial PRIMARY KEY, nombre_entidad varchar(100), lat varchar, long varchar, actividades_economicas JSON, poblacion JSON, patentes JSON, turismo JSON)"
        self.cursor.execute(create_table_command)
        create_table_command = "CREATE TABLE pib_mexico(id serial PRIMARY KEY, ano int, data float)"
        self.cursor.execute(create_table_command)
        print("[✔] Tablas de la bse de datos creadas")

    def limpiar_tablas_postgres(self):
        drop_table_command = "DROP TABLE entidad_federativa"
        self.cursor.execute(drop_table_command)
        drop_table_command = "DROP TABLE pib_mexico"
        self.cursor.execute(drop_table_command)
        print("[✔] Limpieza en las tablas en la base de datos")

    def insertar_entidades_poblacion_2010(self, entidades, poblacion):
        for i, elemento in enumerate(entidades):
            insert_command = "INSERT INTO entidad_federativa(nombre_entidad, poblacion) VALUES('"+elemento+"', '"+json.dumps(poblacion[i])+"')"
            self.cursor.execute(insert_command)
        print("[✔] Indetidades federativas insertados en la base de datos con su poblacion en 2010")
    
    def insertar_poblacion_2010_2017(self, poblacion):
        for x in range(1,33):
            update_command = "UPDATE entidad_federativa SET poblacion='"+json.dumps(poblacion[x-1])+"' WHERE id="+str(x)
            self.cursor.execute(update_command)
        print("[✔] Poblacion hasta el 2017 insertados en la base de datos")
    
    def insertar_poblacion_2018_2019(self, poblacion):
        self.cursor.execute("SELECT * from entidad_federativa")
        entidades_federativas = self.cursor.fetchall()
        for x in range(1, 33):
            contenacion_datos = {**entidades_federativas[x-1][5], **poblacion[x-1]}
            update_command = "UPDATE entidad_federativa SET poblacion='"+json.dumps(contenacion_datos)+"' WHERE id="+str(x)
            self.cursor.execute(update_command)
        print("[✔] Poblacion del 2018 y 2019 insertados en la base de datos")  

    def insertar_patentes_2010_2018(self, patentes):
        for x in range(1, 33):
            update_command = "UPDATE entidad_federativa SET patentes='"+json.dumps(patentes[x-1])+"' WHERE id="+str(x)
            self.cursor.execute(update_command)
        print("[✔] Patentes 2010 hasta el 2018 insetadas en la base de datos")