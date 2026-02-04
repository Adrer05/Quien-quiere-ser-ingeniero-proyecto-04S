import psycopg2

conn = psycopg2.connect(
    dbname="QQSI",
    user="Adrian",
    password="camatagua2505",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT * FROM usuarios")
results = cur.fetchall()
