# test.py

from langgraph_flow import run_graph

if __name__ == "__main__":
    query = "What are the latest use cases of Generative AI in healthcare?"
    result = run_graph(query)
    print("\nFinal Answer:\n", result)
