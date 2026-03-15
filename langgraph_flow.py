

from typing import TypedDict
from langgraph.graph import StateGraph, END
from agents.research_agent import get_research_agent
from agents.answer_agent import get_answer_agent

# Define custom state format
class GraphState(TypedDict):
    query: str
    research_result: str
    answer: str

# Step 1: Research agent node
def run_research_agent(state: GraphState):
    agent = get_research_agent()
    # Use invoke instead of the deprecated run method
    result = agent.invoke({"input": state["query"]})
    return {"research_result": result.get("output", "")}

# Step 2: Answer agent node
def run_answer_agent(state: GraphState):
    chain = get_answer_agent()
    # LCEL pipeline uses invoke
    answer = chain.invoke({
        "query": state["query"],
        "context": state["research_result"]
    })
    return {"answer": answer}

def run_graph(query: str):
    graph = StateGraph(GraphState)

    # Nodes
    graph.add_node("research_agent", run_research_agent)
    graph.add_node("answer_agent", run_answer_agent)

    # Edges
    graph.set_entry_point("research_agent")
    graph.add_edge("research_agent", "answer_agent")
    graph.add_edge("answer_agent", END)

    # Run
    app = graph.compile()
    final_state = app.invoke({"query": query})

    # Return a dictionary directly from the state
    return {
        "answer": final_state.get("answer", ""),
        "research_result": final_state.get("research_result", "")
    }
