# python with database
import psycopg2


def db():
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="12345",
        port="5432"
    )
    print("Connect success", conn)
    conn.close()
    print("Connected")
