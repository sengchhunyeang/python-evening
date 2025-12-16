# default postgresSql :
# port : 5432
# username : postgres
# password :12345
import db
db.db()
import psycopg2
conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="12345",
        port="5432"
    )
cur = conn.cursor()
cur.execute("select * from student")
print(cur.fetchall())