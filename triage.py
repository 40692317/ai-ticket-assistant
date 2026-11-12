import json
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

PROMPT = """You are an IT support assistant. Read the support ticket below.
Reply with ONLY a JSON object, no other text, in exactly this format:
{"category": "...", "priority": "...", "summary": "..."}

category must be one of: Network, Hardware, Software, Account, Other
priority must be one of: Low, Medium, High
summary must be one short sentence.

Ticket:
"""


def triage_ticket(ticket_text):
    response = client.messages.create(
        model="claude-haiku-5-5",
        max_tokens=300,
        messages=[{"role": "user", "content": PROMPT + ticket_text}],
    )
    reply = response.content[0].text
    start = reply.find("{")
    end = reply.rfind("}") + 1
    return json.loads(reply[start:end])


if __name__ == "__main__":
    ticket = "My laptop won't connect to the office Wi-Fi and I have a client meeting in 20 minutes."
    result = triage_ticket(ticket)
    print(result)