# 📚 AI Research Paper Assistant using RAG and Local LLMs

An AI-powered Research Paper Question Answering System built using **Retrieval-Augmented Generation (RAG)**, **FAISS Vector Search**, **Sentence Transformers**, and **TinyLlama Local LLM**.

This application allows users to upload research papers in PDF format and ask natural language questions about the content of the paper.

---

# 🚀 Features

* Upload and analyze research paper PDFs
* Extract text from PDFs using PyMuPDF
* Semantic text chunking for efficient retrieval
* Generate embeddings using Sentence Transformers
* Store embeddings using FAISS vector database
* Semantic similarity search for context retrieval
* Local LLM inference using TinyLlama (No API key required)
* Retrieval-Augmented Generation (RAG) pipeline
* Interactive Streamlit web interface
* Fully offline AI inference after initial model download
* Optimized chunk filtering and retrieval pipeline

---

# 🧠 Tech Stack

| Component       | Technology                |
| --------------- | ------------------------- |
| Frontend        | Streamlit                 |
| PDF Processing  | PyMuPDF                   |
| Embeddings      | Sentence Transformers     |
| Vector Database | FAISS                     |
| Local LLM       | TinyLlama                 |
| NLP Framework   | Hugging Face Transformers |
| Backend         | Python                    |

---

# 🏗️ System Architecture

```text
User Uploads PDF
        ↓
PDF Text Extraction (PyMuPDF)
        ↓
Text Cleaning & Preprocessing
        ↓
Chunking
        ↓
Sentence Transformer Embeddings
        ↓
FAISS Vector Database
        ↓
Semantic Retrieval
        ↓
TinyLlama Local LLM
        ↓
Generated Answer
```

---

# 📂 Project Structure

```text
research-paper-assistant/
│
├── app.py
├── pdf_loader.py
├── vector_store.py
├── rag_pipeline.py
├── requirements.txt
├── README.md
│
├── vector_db/
│
└── venv/
```

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/research-paper-assistant.git
cd research-paper-assistant
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Open your browser:

```text
http://localhost:8501
```

---

# 💡 Example Questions

```text
What problem does this paper solve?
```

```text
Explain the methodology used in the paper.
```

```text
What are the advantages of YOLO?
```

```text
What is self-attention?
```

```text
Summarize this paper in simple language.
```

---

# 🔍 How It Works

## Step 1 — PDF Upload

The user uploads a research paper PDF.

## Step 2 — Text Extraction

PyMuPDF extracts text content from the uploaded paper.

## Step 3 — Text Chunking

The extracted text is split into semantic chunks for efficient retrieval.

## Step 4 — Embedding Generation

Sentence Transformers generate vector embeddings for each chunk.

## Step 5 — Vector Storage

Embeddings are stored in a FAISS vector database.

## Step 6 — Semantic Retrieval

Relevant chunks are retrieved based on similarity with the user query.

## Step 7 — Local LLM Generation

TinyLlama generates contextual answers using the retrieved chunks.

---

# 📈 AI Concepts Implemented

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Embeddings
* Similarity Search
* Local LLM Inference
* Information Retrieval
* NLP Pipelines
* Document Intelligence

---

# 🛠️ Future Improvements

* Multi-PDF Chat Support
* Conversational Memory
* Citation Highlighting
* Research Summarization
* Voice Assistant Integration
* Hugging Face Deployment

---

# 📸 Demo Workflow

1. Upload Research Paper PDF
2. System extracts and indexes content
3. Ask questions in natural language
4. AI generates contextual answers

---

# 📚 Libraries Used

```text
streamlit
transformers
torch
sentence-transformers
faiss-cpu
pymupdf
numpy
```

---

# 🧪 Example Research Papers

## YOLO Paper

[YOLO Research Paper PDF](https://arxiv.org/pdf/1506.02640.pdf?utm_source=chatgpt.com)

## Transformer Paper

[Attention Is All You Need PDF](https://arxiv.org/pdf/1706.03762.pdf?utm_source=chatgpt.com)

## BERT Paper

[BERT Research Paper PDF](https://arxiv.org/pdf/1810.04805.pdf?utm_source=chatgpt.com)

---

# 👩‍💻 Author
Shreya Reja
---

# ⭐ Acknowledgements

* [Hugging Face](https://huggingface.co/?utm_source=chatgpt.com)
* [Streamlit](https://streamlit.io/?utm_source=chatgpt.com)
* [FAISS by Meta AI](https://faiss.ai/?utm_source=chatgpt.com)
* [PyMuPDF Documentation](https://pymupdf.readthedocs.io/?utm_source=chatgpt.com)
