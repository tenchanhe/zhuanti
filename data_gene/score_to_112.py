import sqlite3
import pandas as pd

def get_course():
    connection = sqlite3.connect('data/20230827.db')
    # 建立游標
    cursor = connection.cursor()
    query = "SELECT DISTINCT name,teacher,kind,lmtKind,unit FROM COURSE WHERE y='112';"
    cursor.execute(query)
    course = cursor.fetchall()
    # for row in course:
        # print(row)
    cursor.close()

    connection.close()
    # for C in course:
        # print(C[0], C[1], C[2])
    return course


if __name__ == "__main__":
    file_path = 'data/score.csv'

    df = pd.read_csv(file_path)

    data = []
    
    course = get_course()
    for C in course:
        df.loc[(df['course_name'] == C[0]) & (df['teacher_name'] == C[1]), 'kind'] = int(C[2])
        df.loc[(df['course_name'] == C[0]) & (df['teacher_name'] == C[1]), 'lmtKind'] = C[3]
        df.loc[(df['course_name'] == C[0]) & (df['teacher_name'] == C[1]), 'unit'] = C[4]
        match = df[(df['course_name'] == C[0]) & (df['teacher_name'] == C[1])]

        if not match.empty:
            # match['kind'] = C[2]
            data.append(match)

    df_new = pd.concat(data, ignore_index=True)
    df_new.to_csv('data/score_112.csv', index=False)
