import pandas as pd

file_path = '109選課寶典.csv'
# df = pd.read_csv(file_path)
# 如果需要指定分隔符號，可以使用以下方式，例如使用分號分隔
df = pd.read_csv(file_path, sep=';')

pd.set_option('display.max_rows', None)
# print(df.iloc[10])
# print(df)
# print(df.columns)
# print(df['clm'])
book = []
for line in df['clm']:
    page = ''
    for ch in line:
        if ch != ' ':
            # print(ch, end='')
            page += ch
    book.append(page)
    # print('')

for line in book:
    print(line)
