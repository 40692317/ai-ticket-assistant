import streamlit as st
from triage import triage_ticket

st.title("AI Support Ticket Assistant")
st.write("Paste a support ticket and the AI will sort it by category and priority.")

ticket = st.text_area(
    "Support ticket",
    height=150,
    placeholder="e.g. My laptop won't connect to the office Wi-Fi...",
)

if st.button("Analyse ticket"):
    if not ticket.strip():
        st.warning("Please type a ticket first.")
    else:
        with st.spinner("Asking the AI..."):
            try:
                result = triage_ticket(ticket)
            except Exception:
                st.error("Couldn't get an answer from the AI right now. Please try again.")
                st.stop()

        col1, col2 = st.columns(2)
        col1.metric("Category", result["category"])
        col2.metric("Priority", result["priority"])
        st.write("**Summary:**", result["summary"])