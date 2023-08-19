import sqlite3

db_file = 'score.db'
connection = sqlite3.connect(db_file)
cursor = connection.cursor()

# cursor.execute('''
    # CREATE TABLE IF NOT EXISTS CourseRatings (
        # course_name TEXT,
        # teacher_name TEXT,
        # difficult REAL,
        # busy REAL,
        # low score REAL,
        # high score REAL,
        # easy REAL,
        # interesting REAL,
        # clear REAL,
        # implicit REAL,
        # heavy REAL,
        # boring REAL,
        # thoughtful REAL,
        # sweet REAL,
        # hard REAL,
        # cold REAL,
        # PRIMARY KEY (course_name, teacher_name)
    # )
# ''')

file_path = 'labels_total.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

for i in range (0, len(lines), 6):
    # print(lines[i])
    course_name=''
    teacher_name=''
    list1=[]
    list2=[]
    parts = lines[i].strip().split()  # 按空格分割內容
    course_name, teacher_name = parts[0], parts[1]

    parts = lines[i+1].split('] ')
    part1 = parts[0] + ']'
    part2 = parts[1]
    lista = eval(part1)  # 使用 eval 函式將字符串轉換為列表
    list1 = eval(part2)

    parts = lines[i+2].split('] ')
    part1 = parts[0] + ']'
    part2 = parts[1]
    # listb = eval(part1)
    # list2 = eval(part2)
    lista += eval(part1)
    list1 += eval(part2)
    
    parts = lines[i+3].split('] ')
    part1 = parts[0] + ']'
    part2 = parts[1]
    # listc = eval(part1)
    # list3 = eval(part2)
    lista += eval(part1)
    list1 += eval(part2)
    # print(course_name, teacher_name)
    
    # 將屬性和分數的對應插入表格
    insert_data = [course_name, teacher_name]
    for attribute in ['difficult', 'busy', 'low score', 'high score', 'easy', 'interesting', 'clear', 'implicit', 'heavy', 'boring', 'thoughtful', 'sweet', 'hard', 'cold']:
        insert_data.append(list1[lista.index(attribute)])

    # print(insert_data)
    # cursor.execute('''
        # INSERT INTO CourseRatings (course_name, teacher_name, difficult, busy, low score, high score, easy, interesting, clear, implicit, heavy, boring, thoughtful, sweet, hard, cold)
        # VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    # ''', (insert_data))
    cursor.execute("INSERT INTO CourseRatings VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", insert_data)

# 提交變更並關閉資料庫連接
connection.commit()
connection.close()

print("資料已成功儲存到資料庫。")

