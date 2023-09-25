import sqlite3
import pandas as pd

# 1. 連接到 SQLite 數據庫
conn = sqlite3.connect('score.db')

# 2. 使用 SQL 查詢獲取數據
query = 'SELECT * FROM CourseRatings'

# 3. 使用 pandas 將數據轉換為 DataFrame
df = pd.read_sql_query(query, conn)

# 4. 將 DataFrame 寫入到 Excel 文件
df.to_excel('score.xlsx', index=False)

# 關閉數據庫連接
conn.close()

print('數據已成功輸出到 score.xlsx 文件中。')

