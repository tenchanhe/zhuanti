import sqlite3

connection = sqlite3.connect('course.db')
# 建立游標
cursor = connection.cursor()
query = 'SELECT DISTINCT name, teacher FROM COURSE;'
cursor.execute(query)
course = cursor.fetchall()
# for row in course:
    # print(row)
cursor.close()

connection.close()
for C in course:
    print(C[0], C[1])
