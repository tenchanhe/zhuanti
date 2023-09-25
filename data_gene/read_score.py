import pandas as pd

file_path = 'score.csv'

df = pd.read_csv(file_path, nrows=28)

# print(df['teacher_name'])

for column in df:
    print('\"'+column+'\":[', end='')
    for i in df[column]:
        print('\''+str(i)+'\',', end='')
    print('],')

