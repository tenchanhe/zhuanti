from langchain.embeddings.huggingface_hub import HuggingFaceHubEmbeddings
from langchain.vectorstores.chroma import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain import VectorDBQA, HuggingFaceHub
from langchain.document_loaders import DirectoryLoader
from langchain.chains import RetrievalQA
import os

os.environ['HUGGINGFACEHUB_API_TOKEN'] = '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'

llm = HuggingFaceHub(repo_id = "OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")

loader = DirectoryLoader('data/') #, glob='**/*.json')
documents = loader.load()
print('documents\n', documents)

text_splitter = CharacterTextSplitter()   #chunk_size=100, chunk_overlap=0)
split_docs = text_splitter.split_documents(documents)
#print('split_docs\n', split_docs)

embeddings = HuggingFaceHubEmbeddings()
docsearch = Chroma.from_documents(split_docs, embeddings)
#print('docsearch\n', docsearch)

qa = VectorDBQA.from_chain_type(llm=llm, chain_type="stuff", vectorstore=docsearch,return_source_documents=True)

result = qa({"query": "Which teacher's economics course can get learn a lot?"})
#result = qa({"query": "Which teacher's economics course can get high score?"})
#result = qa({"query": "Which teacher's economics course is better?"})

print(result["query"])
print(result["result"])
#print(result)
