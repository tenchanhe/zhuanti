import pandas as pd

file_path = '../data/score_new.csv'

df = pd.read_csv(file_path)
# print(df)

# for i in range(df.shape[0]):
    # print(df['course_name'][i], df['teacher_name'][i])

for i in df:
    for j in df[i]:
        print(j)
