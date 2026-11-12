import json
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

PROMPT = """You are an IT support assistant. Read the support ticket below.
Reply with ONLY a JSON object, no other text, in exactly this format:
{"category": "...", "priority": "...", "summary": "...", "reply": "..."}

category must be one of: Network, Hardware, Software, Account, Other
priority must be one of: Low, Medium, High
summary must be one short sentence.
reply must be a short, friendly message (2 to 4 sentences) to the person who
raised the ticket. Acknowledge the problem and suggest a sensible first step.

Ticket:
"""


def triage_ticket(ticket_text):
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=600,
        messages=[{"role": "user", "content": PROMPT + ticket_text}],
    )
    raw_text = response.content[0].text
    start = raw_text.find("{")
    end = raw_text.rfind("}") + 1
    return json.loads(raw_text[start:end])


if __name__ == "__main__":
    ticket = "My laptop won't connect to the office Wi-Fi and I have a client meeting in 20 minutes."
    print(triage_ticket(ticket))