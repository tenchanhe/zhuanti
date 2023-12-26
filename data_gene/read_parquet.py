import pandas as pd
from pandas import read_parquet
# data = read_parquet("data/score_112_qa_kind1.parquet", engine='fastparquet')
# data = read_parquet("data/score_112_qa_kind2.parquet", engine='fastparquet')
# data = read_parquet("data/score_112_qa_kind3.parquet", engine='fastparquet')
# data = read_parquet("data/score_112_qa_kind4.parquet", engine='fastparquet')
# data = read_parquet("../data/score_112_qa_all.parquet", engine='fastparquet')
# data = read_parquet("../data/output.parquet", engine='fastparquet')

# data = read_parquet("../data/score_112_text_kind1.parquet", engine='fastparquet')
# data = read_parquet("../data/score_112_text_kind2.parquet", engine='fastparquet')
# data = read_parquet("../data/score_112_text_kind3.parquet", engine='fastparquet')
# data = read_parquet("../data/score_112_text_kind4.parquet", engine='fastparquet')
data = read_parquet("../data/score_112_labels.parquet", engine='fastparquet')
# data = read_parquet("../data/score_112_text_all.parquet", engine='fastparquet')

print(data.count())
for index, row in data.iterrows():
    print(row)

# import pandas as pd

# df1 = pd.read_parquet('../data/score_112_text_kind1.parquet')
# df2 = pd.read_parquet('../data/score_112_text_kind2.parquet')
# df3 = pd.read_parquet('../data/score_112_text_kind3.parquet')
# df4 = pd.read_parquet('../data/score_112_text_kind4.parquet')
# df5 = pd.read_parquet('../data/score_112_text_norate.parquet')

# # 合并数据框
# combined_df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)

# # 保存合并后的数据框为新的 Parquet 文件
# combined_df.to_parquet('../data/score_112_text_all.parquet', index=False)

