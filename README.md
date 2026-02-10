# 🤖 AI Document Q&A Chatbot with RAG

A **Generative AI–powered Document Question & Answering Chatbot** built using **Retrieval-Augmented Generation (RAG)**.  
The system enables accurate, low-latency question answering over private documents by combining vector search with large language models.

---

## 🚀 Key Highlights

- 📄 Built a **GenAI chatbot** using Retrieval-Augmented Generation  
- 🎯 Achieved **95%+ accuracy** on document-based queries  
- ⚡ Sub-2-second response time in production  
- ☁️ Fully deployed on **AWS** with containerized infrastructure  

---

## 🧠 System Architecture

### Retrieval-Augmented Generation (RAG) Pipeline

1. **Document Ingestion**
   - Documents are chunked and embedded using **Amazon Titan Embeddings**

2. **Vector Storage**
   - Embeddings stored in **Amazon OpenSearch (Vector DB)**  
   - Managed through **AWS Bedrock Knowledge Bases**

3. **Query Flow**
   - User query → embedded → vector similarity search  
   - Relevant document chunks retrieved

4. **Answer Generation**
   - Retrieved context passed to **LLM (via AWS Bedrock / OpenAI)**  
   - Final grounded response generated

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **LLMs:** OpenAI / AWS Bedrock  
- **Embeddings:** Amazon Titan  
- **Vector Database:** Amazon OpenSearch  
- **RAG Framework:** LlamaIndex  
- **Deployment:** Docker, AWS EC2  

---

## ⚙️ Deployment

- Dockerized application for portability and scalability  
- Deployed on **AWS EC2**  
- Optimized for:
  - Low latency
  - High retrieval accuracy
  - Production stability

---

## 📊 Performance

| Metric | Result |
|------|-------|
| Document Q&A Accuracy | **95%+** |
| Average Response Time | **< 2 seconds** |
| Retrieval Type | Hybrid Vector Search |

---

## 📌 Use Cases

- Enterprise document Q&A  
- Internal knowledge base assistants  
- Policy and compliance document search  
- Research paper and PDF analysis  

---

## 🔒 Why RAG?

- Prevents hallucinations  
- Grounds answers in real documents  
- Keeps proprietary data private  
- Easily updatable without retraining models  

---


#GenAI #RAG` `#LLM` `#AWS` `#Bedrock` `#OpenSearch` `#LlamaIndex` `#Docker` `#Python`

---
