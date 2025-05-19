import psycopg2

connection = psycopg2.connect(
    database="chinook",
    user="postgres",   # by default is "admin"
    password="admin",  # by default is blank
    host="localhost",  # by default is "localhost", or other DB server
    port="5432"        # by default is "5432"
)

cursor = connection.cursor()
cursor.execute('select * from artist where false')
results = cursor.fetchall()

connection.close()

for result in results:
    print(result)
