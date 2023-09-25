import pandas as pd
from pandas import read_parquet
# data = read_parquet("data/score_112_qa_kind1.parquet", engine='fastparquet')
data = read_parquet("data/score_112_qa_kind2.parquet", engine='fastparquet')
# data = read_parquet("data/score_112_qa_kind3.parquet", engine='fastparquet')
# data = read_parquet("data/score_112_qa_kind4.parquet", engine='fastparquet')
# data = read_parquet("data/score_112_qa_all.parquet", engine='fastparquet')
print(data.count())
# print(data)
for index, row in data.iterrows():
    print(row)

# import pandas as pd

# # 读取四个 Parquet 文件
# df1 = pd.read_parquet('data/score_112_qa_kind1.parquet')
# df2 = pd.read_parquet('data/score_112_qa_kind2.parquet')
# df3 = pd.read_parquet('data/score_112_qa_kind3.parquet')
# df4 = pd.read_parquet('data/score_112_qa_kind4.parquet')

# # 合并数据框
# combined_df = pd.concat([df1, df2, df3, df4], ignore_index=True)

# # 保存合并后的数据框为新的 Parquet 文件
# combined_df.to_parquet('data/score_112_qa_all.parquet', index=False)

