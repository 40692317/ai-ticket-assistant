import pandas as pd
import streamlit as st
from triage import triage_ticket
from database import init_db, save_ticket, get_all_tickets

init_db()

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

        save_ticket(ticket, result)

        col1, col2 = st.columns(2)
        col1.metric("Category", result["category"])
        col2.metric("Priority", result["priority"])
        st.write("**Summary:**", result["summary"])
        st.success("Ticket saved.")

st.divider()
st.subheader("All tickets")

rows = get_all_tickets()
if rows:
    df = pd.DataFrame(rows, columns=["Time", "Category", "Priority", "Summary"])
    st.dataframe(df, hide_index=True)
else:
    st.info("No tickets yet. Analyse one above to get started.")