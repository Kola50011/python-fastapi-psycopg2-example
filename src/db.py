import psycopg2

conn = psycopg2.connect(
    database="service",
    host="localhost",
    user="user",
    password="pass",
    port="5432",
)


def test():
    with conn.cursor() as cursor:
        cursor.execute("select * from information_schema.tables")
        return cursor.fetchall()


def insert():
    with conn.cursor() as cursor:
        cursor.execute("insert into test values ($s, $s)", (1, 1))
