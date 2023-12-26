import sqlite3
import csv

conn = sqlite3.connect('../data/data.db')
cursor = conn.cursor()

with open('../data/score_112_labels.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # 遍历 CSV 文件的每一行
    for row in csv_reader:
        course_name = row['course_name']
        teacher_name = row['teacher_name']
        labels = row['labels']

        # 在数据库中执行更新语句
        cursor.execute("UPDATE COURSE SET labels = ? WHERE name = ? AND teacher = ?", (labels, course_name, teacher_name))


cursor.execute("UPDATE course SET labels = '無' WHERE labels IS NULL")

# 提交更改并关闭连接
conn.commit()
conn.close()

