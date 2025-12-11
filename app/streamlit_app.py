

import sys
import os
from langgraph_flow import run_graph
import streamlit as st

# Append the root project directory to sys.path to access langgraph_flow
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))



st.set_page_config(page_title="AI Research Agent", layout="centered")

st.title("🌐 Deep Research AI Agent")
st.write("Enter a query and let the agents do the research for you.")

query = st.text_input("🔍 Research Query", placeholder="e.g. Impact of LLMs on education")

if st.button("Run Research") and query:
    with st.spinner("Running agents, gathering information..."):
        try:
            result = run_graph(query)
            final_answer = result.get("answer", "No answer generated.")
            research_context = result.get("research_result", "")

            st.success("✅ Research Complete")

            st.markdown("### 📄 Final Answer")
            st.markdown(final_answer)

            st.markdown("---")
            st.markdown("### 🧠 Research Context (Summary)")
            st.markdown(research_context)

        except Exception as e:
            st.error(f"❌ Error occurred: {str(e)}")
