import sqlite3

# 連接到源資料庫 a.db
source_connection = sqlite3.connect('score.db')
source_cursor = source_connection.cursor()

# 連接到目標資料庫 b.db
target_connection = sqlite3.connect('20230827.db')
target_cursor = target_connection.cursor()

# 取得源資料庫中 A 表格的資料
source_cursor.execute('SELECT * FROM CourseRatings')
data_to_copy = source_cursor.fetchall()

# 建立目標資料庫中的 A 表格（如果不存在的話）
target_cursor.execute('''
    CREATE TABLE IF NOT EXISTS CourseRatings (
        course_name TEXT,
        teacher_name TEXT,
        difficult REAL,
        busy REAL,
        low score REAL,
        high score REAL,
        easy REAL,
        interesting REAL,
        clear REAL,
        implicit REAL,
        heavy REAL,
        boring REAL,
        thoughtful REAL,
        sweet REAL,
        hard REAL,
        cold REAL,
        PRIMARY KEY (course_name, teacher_name)
    )
''')

# 將資料複製到目標資料庫的 A 表格
# target_cursor.executemany('INSERT INTO A (column1, column2, ...) VALUES (?, ?, ...)', data_to_copy)
target_cursor.executemany("INSERT INTO CourseRatings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data_to_copy)

# 提交並關閉連接
target_connection.commit()
target_connection.close()
source_connection.close()

