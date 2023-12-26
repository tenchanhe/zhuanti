from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


table_data = [
    {"課名": "管理學", "授課老师": "李瓊淑", "星期": "星期三", "時間":"18-21"},
    {"課名": "經濟學", "授課老师": "蔡致遠", "星期": "星期三", "時間":"9-12"},
    {"課名": "初級會計學（一）", "授課老师": "林禹銘", "星期": "星期一", "時間":"13-16"},
    {"課名": "風水、建築與環境", "授課老师": "邱博舜", "星期": "星期三", "時間":"10-12"}
]


@app.route('/')
def schedule():

    conn = sqlite3.connect('../data/20230827.db')
    cursor = conn.cursor()

    course_info = {}
    for row in table_data:
        # print(row)
        course_name = row["課名"]
        course_teacher = row["授課老师"]
        cursor.execute("SELECT id, teacher, name FROM COURSE WHERE name = ? and teacher = ?", (course_name, course_teacher,))
        result = cursor.fetchone()
        # print(result)
        if result:
            course_info[result[0]] = {
                "id": result[0],
                "teacher": result[1],
                "course": result[2]
            }
    # conn.close()
    # cursor.close()

    return render_template('schedule.html', course_info=course_info)


@app.route('/course/<course>')
def course_detail(course):

    conn = sqlite3.connect('../data/20230827.db')
    cursor = conn.cursor()

    # 在此处查询課程的详细信息
    cursor.execute("SELECT * FROM your_table WHERE course = ?", (course,))
    result = cursor.fetchone()
    # conn.close()
    # cursor.close()
    # 将详细信息传递给 HTML 模板并渲染
    return render_template('course_detail.html', course_data=result)


if __name__ == '__main__':
    app.run(debug=True)

