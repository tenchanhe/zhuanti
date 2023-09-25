from langchain.agents import create_csv_agent
from langchain.llms import HuggingFaceHub
import pandas as pd
import os
os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

# llm = HuggingFaceHub(repo_id = "OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")
llm = HuggingFaceHub(repo_id = "OpenAssistant/falcon-7b-sft-mix-2000", model_kwargs={"temperature":0, "max_length":128})

agent = create_csv_agent(llm, '~/zhuanti_git/data_gene/score.csv', verbose=True)

agent.run("how many rows are there?")
# agent.run("Please give me three 管理學 courses with the highest easy score")
