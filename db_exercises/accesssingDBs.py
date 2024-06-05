import sqlite3

conn = sqlite3.connect('sampledb.db')

cursor = conn.cursor()

# cursor.execute('''
#                DROP TABLE IF EXISTS Counts''')

# cursor.execute('''
#                CREATE TABLE Counts (email TEXT, count INTEGER)''')

email = 'pabs@umich.edu'
cursor.execute('''
               SELECT * FROM Counts where email = ?''', (email,))
row = cursor.fetchone()
if row is None:
    cursor.execute('''
                   INSERT INTO Counts (email, count) VALUES (?, 1)''', (email,))
else: print('A row with this email already exists')

# cursor.execute('''
#                SELECT * FROM Counts''')
# rows = cursor.fetchall()
# cursor.execute('''
#                 UPDATE Counts SET count = count + 1''')
# conn.commit()

for r in cursor.execute('SELECT * FROM Counts ORDER BY count DESC'):
    print(str(r[0]), r[1])



# cursor.execute(
#     '''CREATE TABLE "Users" ("name" TEXT, "email" TEXT)'''
# )

# cursor.execute(
#     '''CREATE TABLE "Countries" ("name" TEXT, "population" INTEGER)'''
# )

# cursor.execute(
#     '''INSERT INTO Users (name, email) VALUES ('Pa s', 'pabs@umich.edu')'''
# )

# cursor.execute('''
#                SELECT * FROM Artist''')
# rows = cursor.fetchall()

# for row in rows:
#     print(type(row))

# print('=============> ', rows)


# for u in users:
#     print(u)

# for i in cursor.execute('select * from Users'):
    # result = cursor.fetchall()
    # print(str(i[0]), str(i[1]))

# print(result)

cursor.close()
conn.close()