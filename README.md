# AI Chatbot

A Retrieval-Augmented Generation (RAG) AI Chatbot built using Python, LangChain, Ollama, ChromaDB, HuggingFace Embeddings, and Streamlit. The chatbot allows users to upload PDF documents and ask questions based on their content.

---

## 🚀 Features

- Upload one or more PDF files
- Permanent storage of uploaded PDFs
- Automatic vector database creation
- Semantic search using ChromaDB
- Local LLM powered by Ollama
- Source document display with every answer
- Chat interface built with Streamlit
- Conversation history
- No internet required after model setup

---

##  Technologies Used

- Python
- Streamlit
- LangChain
- Ollama
- ChromaDB
- HuggingFace Embeddings
- PyPDFLoader


---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/RAG-AI-CHATBOT.git
```

### Move into the project

```bash
cd RAG-AI-CHATBOT
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Install Ollama

Download and install Ollama from:

https://ollama.com

Pull the model:

```bash
ollama pull llama3
```

---

##  Running the Project

Create the vector database:

```bash
python ingest.py
```

Start the Streamlit application:

```bash
streamlit run app.py
```

Open:

```
http://localhost:8501
```

---

##  How to Use

1. Launch the application.
2. Upload one or more PDF documents.
3. Click **Upload PDF**.
4. Wait until the knowledge base is updated.
5. Ask questions about the uploaded documents.
6. The chatbot answers using only the uploaded PDFs.

---

##  Author

**Shiva B**

LinkedIn:
https://www.linkedin.com/in/sivareddy-beemireddy-20920a338

GitHub:
https://github.com/shiva-reddy903
