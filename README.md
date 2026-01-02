
# Comprehensive NLP & AI Agents Learning Roadmap

A structured learning path covering classical NLP, Transformers, LLMs, RAG, Agents, and Orchestration. Use this checklist to track your progress through the curriculum.

## 🟢 Part 1: Foundations of NLP

**Source:** [NLP Demystified](https://www.nlpdemystified.org/course)
*Build the mathematical and conceptual groundwork before diving into LLMs.*

* [] **1. Introduction**
* [ ] **2. Tokenization**
* [ ] **3. Basic Preprocessing**
* [ ] **4. Advanced Preprocessing**
* [ ] **5. Basic Bag-of-Words**
* [ ] **6. TF-IDF**
* [ ] **7. Building Models**
* [ ] **8. Naive Bayes**
* [ ] **9. Topic Modelling**
* [ ] **10. Neural Networks I**
* [ ] **11. Neural Networks II**
* [ ] **12. Word Vectors**
* [ ] **13. Recurrent Neural Networks**
* [ ] **14. Seq2Seq and Attention**
* [ ] **15. Transformers**

---

## 🟡 Part 2: Practical Transformers Ecosystem

**Source:** [Hugging Face NLP Course](https://huggingface.co/learn/nlp-course)
*Learn how to use the standard libraries (Transformers, Datasets, Tokenizers) effectively.*

* [ ] **0. Setup**
* [ ] **1. Transformer models**
* [ ] **2. Using 🤗 Transformers**
* [ ] **3. Fine-tuning a pretrained model**
* [ ] **4. Sharing models and tokenizers**
* [ ] **5. The 🤗 Datasets library**
* [ ] **6. The 🤗 Tokenizers library**
* [ ] **7. Classical NLP tasks**
* [ ] **8. How to ask for help**
* [ ] **9. Building and sharing demos**
* [ ] **10. Curate high-quality datasets**
* [ ] **11. Fine-tune Large Language Models**
* [ ] **12. Build Reasoning Models** *(New)*

---

## 🔵 Part 3: Large Language Models (LLMs)

**Source:** [Cohere LLM University](https://cohere.com/llmu)
*Deep dive into Generative AI, RAG, and Prompt Engineering.*

* [ ] **1. Large Language Models**
* [ ] **2. Text Representation**
* [ ] **3. Text Generation**
* [ ] **4. Deployment**
* [ ] **5. Semantic Search**
* [ ] **6. Prompt Engineering**
* [ ] **7. Retrieval-Augmented Generation (RAG)**
* [ ] **8. Tool Use**
* [ ] **9. Cohere on AWS**

---

## 🟣 Part 4: AI Agents & Frameworks

**Source:** [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/unit1/introduction)
*Moving from static models to autonomous agents.*

### Core Curriculum

* [ ] **Unit 0. Welcome to the course**
* [ ] **Live 1. How the course works and Q&A**
* [ ] **Unit 1. Introduction to Agents**
* [ ] **Unit 2. Frameworks for AI Agents**
* [ ] 2.1 The smolagents framework
* [ ] 2.2 The LlamaIndex framework
* [ ] 2.3 The LangGraph framework


* [ ] **Unit 3. Use Case for Agentic RAG**
* [ ] **Unit 4. Final Project - Create, Test, and Certify Your Agent**

### Bonus Modules

* [ ] **Bonus Unit 1. Fine-tuning an LLM for Function-calling**
* [ ] **Bonus Unit 2. Agent Observability and Evaluation**
* [ ] **Bonus Unit 3. Agents in Games with Pokemon**

---

## 🔴 Part 5: Model Context Protocol (MCP)

**Source:** [Hugging Face MCP Course](https://huggingface.co/learn/mcp-course/unit1/key-concepts)
*Standardizing how AI models interact with data and tools.*

* [ ] **0. Welcome to the MCP Course**
* [ ] **1. Introduction to Model Context Protocol**
* [ ] **2. Use Case: End-to-End MCP Application**
* [ ] **3. Advanced MCP Development: Custom Workflow Servers**
* [ ] 3.1 Use Case: Build a Pull Request Agent on the Hub



---

## 🟠 Part 6: Orchestration Ecosystem

**Source:** [LangChain Ecosystem](https://www.kdnuggets.com/getting-the-most-from-the-langchain-ecosystem)
*Connecting the dots between models, data, and logic.*

* [ ] **Getting The Most From The LangChain Ecosystem**

---
## 🟠 Part 7: LLM fine tuner

**Source:** [Fine Tuning](https://www.youtube.com/watch?v=iOdFUJiB0Zc)
*Connecting the dots between models.*

* [ ] **Getting The Most From The LLM Ecosystem**

---

---

## 📁 Project Files & Notebooks

### NLP Foundations
- [NLP Folder](./NLP/) - Classical NLP implementations and exercises
  - [LLM Basics](./NLP/1-LLM.ipynb) - Introduction to Large Language Models
  - [Text Preprocessing](./NLP/nlp-01-Preprocess.ipynb) - Text cleaning and preparation
  - [Vectorization](./NLP/nlp-02-vectorization.ipynb) - Converting text to numerical representations
  - [Naive Bayes](./NLP/nlp-03-Naive.ipynb) - Classification with Naive Bayes
  - [Topic Modeling (LDA)](./NLP/nlp-04-lda.ipynb) - Latent Dirichlet Allocation
  - [Neural Networks Foundations](./NLP/nlpdemystified_neural_networks_foundations.ipynb) - Basic neural network concepts
  - [Topic Modeling with LDA](./NLP/nlpdemystified_topic_modelling_lda.ipynb) - Advanced topic modeling
  - [Word Vectors](./NLP/nlpdemystified_word_vectors.ipynb) - Word embeddings and vector representations

### Embeddings & Vector Databases
- [PracticeEmbedding Folder](./PracticeEmbedding/) - Working with embeddings and vector stores
  - [ChromaDB Basics](./PracticeEmbedding/chromadbBasics.ipynb) - Vector database operations

### LangChain Framework
- [PracticeLangchain Folder](./PracticeLangchain/) - LangChain implementations
  - [LangChain Basics](./PracticeLangchain/langchainBasic.ipynb) - Core LangChain concepts and usage

### LangGraph & Agent Orchestration
- [PracticeLanggraph Folder](./PracticeLanggraph/) - Graph-based agent workflows
  - [Basic Graph](./PracticeLanggraph/BASICgraph.ipynb) - Introduction to LangGraph

### Retrieval-Augmented Generation (RAG)
- [PracticeRag Folder](./PracticeRag/) - RAG implementations and patterns
  - [RAG Implementation](./PracticeRag/Rag.ipynb) - Basic RAG system
  - [RAG from Scratch (Parts 1-4)](./PracticeRag/rag_from_scratch_1_to_4.ipynb) - Complete RAG tutorial

### Model Context Protocol (MCP)
- [MCP Folder](./MCP/) - Model Context Protocol implementations
  - [MCP Overview](./MCP/MCP.ipynb) - Introduction to MCP concepts
  - [JPMC MCP Project](./MCP/jpmcMCP/) - Complete MCP server/client implementation

### AI Agents & Applications
- [RegGuard Project](./MCP/GSRegGuard/) - Regulatory compliance agent
  - [Flask Application](./MCP/GSRegGuard/app.py) - Main application server
  - [Agent Configuration](./MCP/GSRegGuard/auto/agent.json) - Agent setup and parameters
  - [Manual Agent Client](./MCP/GSRegGuard/manual-agent-client/) - Client implementation

---
