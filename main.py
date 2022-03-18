import psycopg2

connection = psycopg2.connect(database="DataBase", user="UserName", password="Password", host="Host", port="5432")

cursor = connection.cursor()

cursor.execute("SELECT * FROM users")

for currentUser in cursor:
    print(currentUser[0], " ", currentUser[1], " ", currentUser[2], " ", currentUser[3])

cursor.execute("INSERT INTO users (login, password, name) VALUES (%s, %s, %s)", ("user2", "user2", "user2"))
connection.commit()

cursor.execute("SELECT * FROM users")

for currentUser in cursor:
    print(currentUser[0], " ", currentUser[1], " ", currentUser[2], " ", currentUser[3])

cursor.close()

with connection:
    with connection.cursor() as cur:
        try:
            cur.execute("DELETE FROM users")
            cur.execute()
            cur.execute()
        except:
            connection.rollback()

connection.close()