import sqlite3
import pandas as pd


def get_len_all():
    conn = sqlite3.connect('../data/20230827.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT name, COUNT(DISTINCT id) AS course_count
        FROM course
        WHERE y=112
        GROUP BY name
        ORDER BY course_count DESC;
    ''')

    results = cursor.fetchall()
    conn.close()
    
    data = {'course_name':[], 'num':[]}
    for row in results:
        # print(row[0], row[1])
        data['course_name'].append(row[0])
        data['num'].append(row[1])


    new_df = pd.DataFrame(data)
    new_df.to_csv('../data/course_len_112_all.csv', index=False)


def get_len_kind2():
    conn = sqlite3.connect('../data/20230827.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT unit, COUNT(DISTINCT id) AS course_count
        FROM course
        WHERE y=112 and kind=2
        GROUP BY unit
        ORDER BY course_count DESC;
    ''')

    results = cursor.fetchall()
    conn.close()
    
    data = {'unit':[], 'num':[]}
    for row in results:
        # print(row[0], row[1])
        data['unit'].append(row[0])
        data['num'].append(row[1])


    new_df = pd.DataFrame(data)
    new_df.to_csv('../data/course_len_112_kind2.csv', index=False)


def get_len_kind3():
    conn = sqlite3.connect('../data/20230827.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT unit, COUNT(DISTINCT id) AS course_count
        FROM course
        WHERE y=112 and kind=3
        GROUP BY unit
        ORDER BY course_count DESC;
    ''')

    results = cursor.fetchall()
    conn.close()
    
    data = {'unit':[], 'num':[]}
    for row in results:
        # print(row[0], row[1])
        data['unit'].append(row[0])
        data['num'].append(row[1])


    new_df = pd.DataFrame(data)
    new_df.to_csv('../data/course_len_112_kind3.csv', index=False)


def get_len_kind4():
    conn = sqlite3.connect('../data/20230827.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT lmtKind, COUNT(DISTINCT id) AS course_count
        FROM course
        WHERE y=112 and kind=4
        GROUP BY lmtKind
        ORDER BY course_count DESC;
    ''')

    results = cursor.fetchall()
    conn.close()
    
    data = {'lmtKind':[], 'num':[]}
    for row in results:
        # print(row[0], row[1])
        data['lmtKind'].append(row[0])
        data['num'].append(row[1])


    new_df = pd.DataFrame(data)
    new_df.to_csv('../data/course_len_112_kind4.csv', index=False)


if __name__ == "__main__":
    # get_len_all()
    # get_len_kind2()
    # get_len_kind3()
    get_len_kind4()
