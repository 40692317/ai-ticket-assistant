from datetime import datetime

import pandas as pd
import streamlit as st
from triage import triage_ticket
from database import init_db, save_ticket

MAX_TICKETS_PER_SESSION = 5

init_db()

if "tickets_used" not in st.session_state:
    st.session_state.tickets_used = 0
if "my_tickets" not in st.session_state:
    st.session_state.my_tickets = []

st.title("AI Support Ticket Assistant")
st.write("Paste a support ticket and the AI will sort it and draft a reply.")

ticket = st.text_area(
    "Support ticket",
    height=150,
    max_chars=1000,
    placeholder="e.g. My laptop won't connect to the office Wi-Fi...",
)

if st.button("Analyse ticket"):
    remaining = MAX_TICKETS_PER_SESSION - st.session_state.tickets_used
    if not ticket.strip():
        st.warning("Please type a ticket first.")
    elif remaining <= 0:
        st.warning("You've reached the demo limit for this session. Thanks for trying it!")
    else:
        with st.spinner("Asking the AI..."):
            try:
                result = triage_ticket(ticket)
            except Exception:
                st.error("Couldn't get an answer from the AI right now. Please try again.")
                st.stop()

        st.session_state.tickets_used += 1
        save_ticket(ticket, result)
        st.session_state.my_tickets.insert(0, (
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            result["category"],
            result["priority"],
            result["summary"],
        ))

        col1, col2 = st.columns(2)
        col1.metric("Category", result["category"])
        col2.metric("Priority", result["priority"])
        st.write("**Summary:**", result["summary"])

        st.subheader("Suggested reply")
        st.info(result["reply"])
        st.success("Ticket saved.")

left = MAX_TICKETS_PER_SESSION - st.session_state.tickets_used
st.caption(f"Demo limit: {left} of {MAX_TICKETS_PER_SESSION} tickets left this session.")

st.divider()
st.subheader("Your tickets this session")
st.caption("Only you can see these. Other visitors see only their own.")

if st.session_state.my_tickets:
    df = pd.DataFrame(
        st.session_state.my_tickets,
        columns=["Time", "Category", "Priority", "Summary"],
    )
    st.dataframe(df, hide_index=True)
else:
    st.info("No tickets yet. Analyse one above to get started.")