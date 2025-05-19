import psycopg2

connection = psycopg2.connect(
    database="chinook",
    user="postgres",   # by default is "admin"
    password="admin",  # by default is blank
    host="localhost",  # by default is "localhost", or other DB server
    port="5432"        # by default is "5432"
)

cursor1 = connection.cursor()
cursor1.execute('select * from artist')
results1 = cursor1.fetchall()

cursor2 = connection.cursor()
cursor2.execute('select * from artist where name = %s', ["Queen"])
results2 = cursor2.fetchall()

cursor3 = connection.cursor()
cursor3.execute('select * from artist where artist_id = %s', [51])
results3 = cursor3.fetchall()

cursor4 = connection.cursor()
cursor4.execute('select count(*) from artist')
results4 = cursor4.fetchone()

connection.close()

for result in results1:
    print(result)

print("++++++++++++++++++++++++++++++++")

for result in results2:
    print(result)

print("++++++++++++++++++++++++++++++++")

for result in results3:
    print(result)

    print("++++++++++++++++++++++++++++++++")

for result in results4:
    print(result)
