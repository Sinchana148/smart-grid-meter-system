import psycopg2

conn = psycopg2.connect(
    dbname="smart_grid_db",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()