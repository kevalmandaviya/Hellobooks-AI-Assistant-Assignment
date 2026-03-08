import os
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

documents = []

data_folder = "data"

for file in os.listdir(data_folder):
    loader = TextLoader(os.path.join(data_folder, file))
    documents.extend(loader.load())

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = FAISS.from_documents(documents, embeddings)

vectorstore.save_local("vectorstore")

print("Vector database created successfully!")