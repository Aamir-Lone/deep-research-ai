
# 🧠 AI Agent-Based Deep Research

This project is a dual-agent research system built using **LangGraph** and **LangChain** with **Together.ai** as the LLM provider. It is designed to accept a query, perform live web research using the **Tavily Search API**, and generate a polished final answer.

---

## 📌 Features

- 🔍 Autonomous Web Search (via Tavily API)
- 🧠 Two-Agent Research & Answering System
- 🌐 Uses LangGraph for agent orchestration
- 🤖 Together.ai for LLM-based reasoning
- ✅ Clean modular codebase (easy to extend)
- 🧪 CLI interface and 🌐 Streamlit UI for testing

---

## 🌐 Live Demo

Test the app directly in your browser:

👉 [**Click here to run the Streamlit app**](https://deep-research-ai-jqqhbf7ggrt2x3tsse2yks.streamlit.app/)

---

## 📁 Directory Structure

```
deep-research-ai/
│
├── agents/
│   ├── research_agent.py       # Gathers information from Tavily Search
│   ├── answer_agent.py         # Compiles and summarizes the final answer
│
├── app/
│   └── streamlit_app.py        # Streamlit frontend for user input/output
│
├── langgraph_flow.py           # LangGraph state machine and pipeline runner
├── prompt_templates.py         # Templates used by agents for prompting
├── .env                        # Handles environment variables
├── test.py                     # CLI entry point to run the full pipeline
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview and documentation
```

---

## 📦 Dependencies

Install the following dependencies using pip. These are already listed in `requirements.txt`.

```text
streamlit
langchain
langgraph
langchain_together
tavily-python
python-dotenv
langchain-community
openai

```

Install all with:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Setup

Set your API keys for Together.ai and Tavily. :

 Use `.env` file
Create a file named `.env` and add:
```
TOGETHER_API_KEY=your_together_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ⚙️ How It Works

### 🧠 Agents

- **Research Agent**:
  - Uses Tavily API to search the web.
  - Extracts and formats relevant data.

- **Answer Agent**:
  - Uses Together.ai LLM to read search results.
  - Drafts a final, comprehensive response.

### 🔄 LangGraph Flow

LangGraph organizes the process into a state machine with the following steps:

1. Accept user query
2. Use `research_agent` to get web data
3. Use `answer_agent` to analyze and summarize
4. Return a refined answer

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/Aamir-Lone/deep-research-ai.git
cd deep-research-ai
```

### 2. (Optional) Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Unix/macOS
venv\Scripts\activate        # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

create a `.env` file 

### 5. Run via Streamlit (Recommended)

```bash
streamlit run app/streamlit_app.py
```

### 6. Run via CLI (Optional)

```bash
python test.py
```

You’ll be prompted to enter a query in the terminal and see results printed after research.

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

## 🧑‍💻 Author

**Aamir Lone**  
📫 [View Live Demo](https://deep-research-ai-jqqhbf7ggrt2x3tsse2yks.streamlit.app/)

---

