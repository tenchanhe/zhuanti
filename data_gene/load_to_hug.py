from datasets import load_dataset
from pandas import read_parquet

dataset = load_dataset("ChanHE/data_for_rag")
# print(dataset)
# dataset = read_parquet("finetune_data.parquet")

# dataset.push_to_hub("ChanHE/data_for_rag/data")
