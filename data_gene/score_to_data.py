import pandas as pd

file_path = '../data/score_realscore.csv'

df = pd.read_csv(file_path)

column = []
for i in df:
    column.append(i)

tmp = column[0]
column[0] = column[1]
column[1] = tmp
# print(column)

words = ['老師的','課程']
column_zh = ['teacher_name','course_name','困難','繁忙','低分','高分','容易','有趣','清楚','模糊','負擔重','無聊','親切','甜','硬','涼']
data = {'text':[]}

for i in range(df.shape[0]):
    line = ''
    for j in range(len(column)):
        if j<=1:
            line += df[column[j]][i] + words[j] + ', '
        elif j==len(column)-1:
            line += column_zh[j] + ':' + str(df[column[j]][i]) + '.'
        else:
            line += column_zh[j] + ':' + str(df[column[j]][i]) + ', '
    # print(line)
    data['text'].append(line)

# print(data)
data = pd.DataFrame(data)
data.to_csv('../data/score_rag_2.csv', index=False)
