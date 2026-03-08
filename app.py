from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


db = FAISS.load_local("vectorstore", embeddings, allow_dangerous_deserialization=True)

print("AI Accounting Assistant Ready!")

while True:
    question = input("\nAsk accounting question: ")

    docs = db.similarity_search(question)

    print("\nRelevant Information:\n")

    for doc in docs:
        print(doc.page_content)