import pandas as pd

# file_path = './score_test.csv'
file_path = './score_realscore.csv'

df = pd.read_csv(file_path)

column = []
for i in df:
    column.append(i)

tmp = column[0]
column[0] = column[1]
column[1] = tmp

words = ['老師的','課程']
data = {'text':[]}

for i in range(df.shape[0]):
    line = ''
    for j in range(len(column)):
        if j<=1:
            line += df[column[j]][i] + words[j]
        elif j==len(column)-1:
            line += column[j] + '分數為' + str(df[column[j]][i]) + '.'
        else:
            line += column[j] + '分數為' + str(df[column[j]][i]) + ','
    # print(line)
    data['text'].append(line)

# print(data)
data = pd.DataFrame(data)
data.to_csv('./score_rag_2.csv', index=False)
