from langchain import HuggingFaceHub, SQLDatabase, SQLDatabaseChain
import os

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

llm = HuggingFaceHub(repo_id = "OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")
#llm = HuggingFaceHub(repo_id = "OpenAssistant/llama2-13b-orca-8k-3319")
#llm = HuggingFaceHub(repo_id = "meta-llama/Llama-2-7b-chat-hf")

#input_db = SQLDatabase.from_uri("sqlite:///course.db")
input_db = SQLDatabase.from_uri("sqlite:///titanic.db")
print('hi ', input_db._schema)


db_agent = SQLDatabaseChain(llm = llm, database = input_db, verbose=True)

#db_agent.run("how many rows are there in table COURSE?")
db_agent.run("how many rows are there in table?")
#db_agent.run("How many passengers were in each class?")
