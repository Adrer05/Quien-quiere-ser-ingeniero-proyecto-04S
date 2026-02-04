import os
os.system("cls")
import psycopg2

conn = psycopg2.connect(
    dbname="QQSI",
    user="Adrian",
    password="camatagua2505",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()
cursor.execute("INSERT INTO usuario (nombre, apellido, usuario) values (%s, %s, %s)", ("Adrian","Ferrer","Adrer"))
conn.commit()
cursor.execute("SELECT * FROM usuario")
results = cursor.fetchall()
print(results)