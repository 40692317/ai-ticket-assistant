import json
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

VALID_CATEGORIES = {"Network", "Hardware", "Software", "Account", "Other"}
VALID_PRIORITIES = {"Low", "Medium", "High"}

PROMPT = """You are an IT support assistant. Read the support ticket below.
Reply with ONLY a JSON object, no other text, in exactly this format:
{"category": "...", "priority": "...", "summary": "...", "reply": "..."}

category must be one of: Network, Hardware, Software, Account, Other
   priority must be one of: Low, Medium, High, using these rules:
   - High: many people are affected, there is a security risk, or there is an urgent deadline today.
   - Medium: one person cannot work properly, with no urgent deadline.
   - Low: a minor issue, a question, or a request for something new.
summary must be one short sentence.
reply must be a short, friendly message (2 to 4 sentences) to the person who
raised the ticket. Acknowledge the problem and suggest a sensible first step.

Ticket:
"""


def parse_response(raw_text):
    """Turn the AI's text into a clean dictionary, with a safety net."""
    start = raw_text.find("{")
    end = raw_text.rfind("}") + 1
    if start == -1 or end == 0:
        raise ValueError("No JSON found in the AI response")

    data = json.loads(raw_text[start:end])

    if data.get("category") not in VALID_CATEGORIES:
        data["category"] = "Other"
    if data.get("priority") not in VALID_PRIORITIES:
        data["priority"] = "Medium"
    data.setdefault("summary", "")
    data.setdefault("reply", "")
    return data


def triage_ticket(ticket_text):
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=600,
        messages=[{"role": "user", "content": PROMPT + ticket_text}],
    )
    raw_text = "".join(
        block.text for block in response.content if block.type == "text"
    )
    return parse_response(raw_text)


if __name__ == "__main__":
    ticket = "My laptop won't connect to the office Wi-Fi and I have a client meeting in 20 minutes."
    print(triage_ticket(ticket))