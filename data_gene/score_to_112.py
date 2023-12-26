import sqlite3
import pandas as pd

def get_course():
    connection = sqlite3.connect('../data/20230827.db')
    cursor = connection.cursor()
    # have_rate
    # query = "SELECT DISTINCT name,teacher,kind,lmtKind,unit FROM COURSE WHERE y='112';"
    
    # no_have_rate
    query = "SELECT DISTINCT name,teacher FROM COURSE WHERE y='112';"
    cursor.execute(query)
    course = cursor.fetchall()
    print(len(course))
    # for row in course:
        # print(row)
    cursor.close()

    connection.close()
    # for C in course:
        # print(C[0], C[1], C[2])
    return course


def have_rate(course):
    file_path = '../data/score_new.csv'
    df = pd.read_csv(file_path)
    data = []
    # 加欄位
    for C in course:
        df.loc[(df['course_name'] == C[0]) & (df['teacher_name'] == C[1]), 'kind'] = int(C[2])
        df.loc[(df['course_name'] == C[0]) & (df['teacher_name'] == C[1]), 'lmtKind'] = C[3]
        df.loc[(df['course_name'] == C[0]) & (df['teacher_name'] == C[1]), 'unit'] = C[4]
        match = df[(df['course_name'] == C[0]) & (df['teacher_name'] == C[1])]

        if not match.empty:
            # match['kind'] = C[2]
            data.append(match)

    df_new = pd.concat(data, ignore_index=True)
    df_new.to_csv('../data/score_112_haverate.csv', index=False)


def no_have_rate(course):
    file_path = '../data/score_112_haverate.csv'
    df = pd.read_csv(file_path)
    data = {'course_name':[], 'teacher_name':[]}
    # print(df.shape[0])
    # print(course)
    for i in range(df.shape[0]):
        tup = (df['course_name'][i], df['teacher_name'][i])
        # print(tup)
        if tup in course:
            course.remove(tup)

    # print(data)
    # print(course)
    new_data = pd.DataFrame(course)
    new_data.to_csv('../data/score_112_norate.csv', index=False)


if __name__ == "__main__":
    
    course = get_course()
    # have_rate(course)
    no_have_rate(course)
