# Hellobooks AI Assistant
This project is a mini AI assistant built for a **Python Developer Internship Assignment**.  
It answers basic **accounting-related questions** using a **Retrieval-Augmented Generation (RAG)** approach.

## Technologies Used

- Python
- LangChain
- FAISS (Vector Database)
- HuggingFace Embeddings
- Sentence Transformers
- Docker

## Project Structure

hellobooks-ai-assistant
│
├── data
│ ├── bookkeeping.txt
│ ├── invoices.txt
│ ├── profit_loss.txt
│ ├── balance_sheet.txt
│ └── cash_flow.txt
│
├── vectorstore
├── app.py
├── build_vector_db.py
├── requirements.txt
├── Dockerfile
└── README.md

## Setup

Install dependencies:
pip install -r requirements.txt
Build vector database:
python build_vector_db.py
Run the assistant:
python app.py

## Example Questions

- What is bookkeeping?
- What is profit and loss?
- Explain balance sheet
- What is cash flow?

## RAG Flow
User Question → Vector Search (FAISS) → Retrieve Documents → Return Relevant Information

---

Author: Keval Mandaviya
