import pandas as pd

with open('source_finetune_data.txt', 'r') as file:
    content = file.read()

qa_pairs = content.strip().split('\n\n')

data = {'question':[], 'answer':[], 'text':[]}
for qa_pair in qa_pairs:
    question, answer = qa_pair.split('\n')
    data['question'].append(question)
    data['answer'].append(answer)
    data['text'].append("<s>[INST] " + question + " [/INST]" + answer + " </s>")

df = pd.DataFrame(data)
# print(df)
# print(df['text'])

# 將 DataFrame 寫入 Parquet 格式檔案
df.to_parquet('rag_data.parquet', index=False)
