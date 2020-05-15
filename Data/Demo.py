import psycopg2

conn = psycopg2.connect(database="cqubedev", user = "cqubedev", password = "tibil123", host = "jdbc:postgresql://localhost"
, port = "5432")

print("Opened database successfully")


