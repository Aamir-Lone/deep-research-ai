# 🧠 AI Agent-Based Deep Research

This project is a dual-agent research system built using **LangGraph** and **LangChain** with **Together.ai** as the LLM provider. It is designed to accept a query, perform live web research using the **Tavily Search API**, and generate a polished final answer.

---

## 📌 Features

- 🔍 Autonomous Web Search (via Tavily API)
- 🧠 Two-Agent Research & Answering System
- 🌐 Uses LangGraph for agent orchestration
- 🤖 Together.ai for LLM-based reasoning
- ✅ Clean modular codebase (easy to extend)
- 📄 CLI interface for demo/testing

---

## 📁 Directory Structure

```
deep-research-ai/
│
├── agents/
│   ├── research_agent.py       # Gathers information from Tavily Search
│   └── answer_agent.py         # Compiles and summarizes the final answer
│
├── prompt_template.py          # Templates used by agents for LLM prompting
├── langgraph_flow.py           # Defines the LangGraph state graph and agent transitions
├── test.py                     # CLI entrypoint to run the full pipeline
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview and documentation
```

---

## 📦 Dependencies

Install the following dependencies using pip. They are listed in `requirements.txt`.

```text
langchain
langgraph
together
tavily-python
openai
```

You can install all dependencies using:

```bash
pip install -r requirements.txt
```

> 🔐 Make sure to set your API keys for Together.ai and Tavily:
```bash
export TOGETHER_API_KEY=your_together_api_key
export TAVILY_API_KEY=your_tavily_api_key
```

---

## ⚙️ How It Works

### 🧠 Agents

- **Research Agent**:
  - Uses Tavily Search API to search the web.
  - Extracts and formats raw content for the Answer Agent.

- **Answer Agent**:
  - Uses Together.ai LLM to read search results.
  - Generates a complete and structured answer.

### 🔄 LangGraph Flow

LangGraph defines a state machine with the following flow:

1. Start with a `query`
2. Pass query to `research_agent`
3. Get search results
4. Pass results to `answer_agent`
5. Return final summarized answer

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Aamir-Lone/deep-research-ai.git
cd deep-research-ai
```

### 2. Setup Python Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # on Unix
venv\Scripts\activate     # on Windows
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

```bash
export TOGETHER_API_KEY=your_together_api_key
export TAVILY_API_KEY=your_tavily_api_key
```

### 5. Run the System

Use the `test.py` script to test the pipeline:

```bash
python test.py
```

You’ll be prompted to enter a research question. The system will:
1. Search the web
2. Summarize findings
3. Display the final answer

---

## 🧪 Sample Input & Output

**Input**:
```
What are the recent use cases of Generative AI in healthcare?
```

**Output**:
```
1. Medical Imaging Analysis
2. Clinical Decision Support
3. Synthetic Data Generation
4. Automation of Clinical Documentation
5. Drug Discovery
6. Personalized Medicine

```

---



