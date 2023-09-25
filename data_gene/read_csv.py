import pandas as pd

file_path = 'data/score_112.csv'

df = pd.read_csv(file_path)
# print(df)

for i in range(df.shape[0]):
    if df['course_name'][i] == '中級會計學（一）':
        print(df['course_name'][i], df['teacher_name'][i])
