# 🏭 Industrial Knowledge Intelligence Platform

> A Multi-Agent Hybrid RAG system for intelligent industrial document understanding, maintenance diagnostics, compliance validation, and continuous knowledge evolution.

---

## 📌 Overview

Industrial Knowledge Intelligence Platform is an AI-powered document intelligence system that combines **Universal Document Ingestion**, **Knowledge Graphs**, **Hybrid Retrieval-Augmented Generation (RAG)**, and **Multi-Agent Systems** to answer engineering queries with high contextual accuracy.

The platform supports multiple industrial document formats and enables intelligent retrieval, maintenance reasoning, compliance analysis, lessons learned exploration, and engineer-driven knowledge updates.

---

## ✨ Key Features

* 📄 Universal Document Ingestion (PDF, DOCX, PPTX, CSV, XLSX, TXT)
* 🧩 Automatic Chunking and Metadata Extraction
* 🏷️ Entity Extraction and Knowledge Graph Construction
* 🔎 Hybrid Retrieval using Knowledge Graphs and FAISS
* 🎯 CrossEncoder Re-ranking for improved retrieval quality
* 🤖 LLM-based Intelligent Query Routing
* 🧠 Multi-Agent Reasoning
* 🔧 Maintenance Diagnostics
* 📋 Compliance Validation
* 📚 Lessons Learned Analysis
* 🔄 "Updated at the Point of Need" through Engineer Feedback
* 💻 Interactive Streamlit Interface

---

# 🏗️ System Architecture

```text
                   Industrial Documents
                            │
                            ▼
             Universal Document Ingestion
                            │
                            ▼
      Chunking • Metadata • Entity Extraction
              │                       │
              ▼                       ▼
      Knowledge Graph           Embeddings
                                      │
                                      ▼
                               FAISS Vector Store
                                      │
                                      ▼
                           Hybrid Retrieval Engine
                                      │
                                      ▼
                        CrossEncoder Re-ranking
                                      │
                                      ▼
                            LLM Router Agent
                                      │
      ┌──────────────┬──────────────┬──────────────┬──────────────┐
      ▼              ▼              ▼              ▼
 Knowledge      Maintenance     Compliance   Lessons Learned
   Agent            Agent          Agent          Agent
                                      │
                                      ▼
                              Final Response
                                      │
                                      ▼
                           Engineer Feedback
                                      │
                                      ▼
                                Update Agent
                                      │
             Knowledge Graph + FAISS Updated Dynamically
```

---

# 🤖 Multi-Agent Architecture

| Agent                 | Responsibility                                                |
| --------------------- | ------------------------------------------------------------- |
| Knowledge Agent       | Answers general engineering questions                         |
| Maintenance Agent     | Root cause analysis and maintenance recommendations           |
| Compliance Agent      | Standards, regulations, and compliance validation             |
| Lessons Learned Agent | Similar incidents and preventive recommendations              |
| Router Agent          | Routes queries to the appropriate specialist agent            |
| Update Agent          | Updates the Knowledge Graph and FAISS using engineer feedback |

---

# 🔍 Hybrid RAG Pipeline

1. Universal Document Ingestion
2. Document Chunking
3. Metadata Extraction
4. Entity Extraction
5. Knowledge Graph Construction
6. Embedding Generation
7. FAISS Index Creation
8. Hybrid Retrieval
9. CrossEncoder Re-ranking
10. LLM-based Response Generation
11. Engineer Feedback & Knowledge Update

---

# 💻 Tech Stack

| Category        | Technologies          |
| --------------- | --------------------- |
| Programming     | Python                |
| UI              | Streamlit             |
| LLM             | Ollama, Mistral       |
| Embeddings      | Sentence Transformers |
| Vector Search   | FAISS                 |
| Knowledge Graph | NetworkX              |
| NLP             | spaCy                 |
| Re-ranking      | CrossEncoder          |
| Retrieval       | Hybrid RAG            |
| Architecture    | Multi-Agent Systems   |

---

# 📁 Project Structure

```text
industrial-knowledge-intelligence/
│
├── agents/
│   ├── knowledge_analyze.py
│   ├── maintenance_agent.py
│   ├── compliance_agent.py
│   ├── lessons_agent.py
│   ├── router_agent.py
│   └── update_agent.py
│
├── utils/
├── data/
├── app.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

```bash
git clone https://github.com/mulelikitha-hue/industrial-knowledge-intelligence.git

cd industrial-knowledge-intelligence

pip install -r requirements.txt

streamlit run app.py
```

---

# 📖 Workflow

1. Upload industrial documents.
2. Documents are parsed and chunked.
3. Metadata and entities are extracted.
4. Knowledge Graph and FAISS index are created.
5. User submits a query.
6. Router Agent selects the appropriate specialist agent.
7. Hybrid Retrieval fetches relevant context.
8. CrossEncoder re-ranks retrieved documents.
9. LLM generates the final response.
10. Engineer feedback dynamically updates the Knowledge Graph and FAISS index.

---

# 📸 Screenshots

> Add screenshots of:
>
> * Document Upload
> * Query Processing
> * Retrieved Context
> * Multi-Agent Response
> * Engineer Feedback & Knowledge Update

---

# 🎯 Future Enhancements

* Persistent Vector Database
* Conversation Memory
* Role-Based Access Control
* Cloud Deployment
* Incremental Indexing
* Advanced Analytics Dashboard

---

# 👨‍💻 Author

**Mule Kowshik**

GitHub: https://github.com/mulelikitha-hue
