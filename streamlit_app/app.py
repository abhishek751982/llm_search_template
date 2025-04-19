import streamlit as st
import requests

st.title("🔍 LLM-based RAG Search")

# Input for user query
query = st.text_input("Enter your query:")

if st.button("Search") and query:
    flask_url = "http://localhost:5001/query"
    st.write(f"📡 Sending query to backend: `{query}`")

    try:
        # Make POST request to Flask API
        response = requests.post(flask_url, json={"query": query})
        
        # Check if response was returned
        if response and response.status_code == 200:
            answer = response.json().get('answer', "No answer received.")
            st.success("✅ Answer received:")
            st.markdown(f"**{answer}**")
        else:
            st.error(f"❌ Backend returned status code: {response.status_code if response else 'None'}")

    except Exception as e:
        st.error(f"❗ Could not connect to backend: {e}")
