

from langgraph.graph import StateGraph, END
from langchain.schema.runnable import RunnableLambda
from agents.research_agent import get_research_agent
from agents.answer_agent import get_answer_agent

# Define custom state format
class GraphState(dict):
    query: str
    research_result: str
    answer: str

# Step 1: Research agent node
def run_research_agent(state):
    agent = get_research_agent()
    result = agent.run(state["query"])
    state["research_result"] = result
    return state

# Step 2: Answer agent node
def run_answer_agent(state):
    chain = get_answer_agent()
    answer = chain.run({
        "query": state["query"],
        "context": state["research_result"]
    })
    state["answer"] = answer
    return state

def run_graph(query: str):
    graph = StateGraph(GraphState)

    # Nodes
    graph.add_node("research_agent", RunnableLambda(run_research_agent))
    graph.add_node("answer_agent", RunnableLambda(run_answer_agent))

    # Edges
    graph.set_entry_point("research_agent")
    graph.add_edge("research_agent", "answer_agent")
    graph.add_edge("answer_agent", END)

    # Run
    app = graph.compile()
    final_state = app.invoke({"query": query})

    # Return a dictionary instead of raw string
    return {
        "answer": final_state["answer"],
        "research_result": final_state.get("research_result", None)
    }
