import sqlite3
import csv

# 連接到 SQLite 數據庫文件
conn = sqlite3.connect('score.db')
cursor = conn.cursor()

# 執行 SQL 查詢，獲取數據
cursor.execute('SELECT * FROM CourseRatings')  # 請將 your_table_name 替換為實際的表格名稱
data = cursor.fetchall()

# 關閉數據庫連接
conn.close()

# 將數據輸出到 CSV 文件
with open('score.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    # 寫入 CSV 文件的標題行
    column_names = [description[0] for description in cursor.description]
    csvwriter.writerow(column_names)
    
    # 寫入數據行
    csvwriter.writerows(data)

print("數據已成功輸出到 output.csv 文件中。")

