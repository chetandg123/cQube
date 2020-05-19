
import psycopg2

conn = psycopg2.connect(database="cqubedev", user = "cqubedev", password = "tibil123", host ="localhost", port = "5432")
print("Database Connected....")
conn.commit()

