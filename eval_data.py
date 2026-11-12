# Each test: (ticket text, correct category, correct priority)
# Priority guide used for labelling:
#   High   = many people affected, a security risk, or an urgent deadline
#   Medium = one person can't work properly
#   Low    = minor issue, question, or request

TEST_TICKETS = [
    # Network
    ("The whole office has lost internet and nobody can work.", "Network", "High"),
    ("My laptop won't connect to the office Wi-Fi, but my phone connects fine.", "Network", "Medium"),
    ("The VPN keeps disconnecting every 10 minutes when I work from home.", "Network", "Medium"),
    ("Wi-Fi is a bit slow in the meeting room on the second floor.", "Network", "Low"),
    ("Nobody on the third floor can reach the shared drive because the network is down.", "Network", "High"),
    ("Can you give me the guest Wi-Fi password for a visitor coming tomorrow?", "Network", "Low"),
    # Hardware
    ("My laptop screen is cracked and I can't see anything on it.", "Hardware", "Medium"),
    ("The printer keeps saying paper jam but nothing is stuck.", "Hardware", "Medium"),
    ("The spacebar on my keyboard is a bit sticky.", "Hardware", "Low"),
    ("My laptop won't turn on at all and I'm presenting to a client in one hour.", "Hardware", "High"),
    ("Could I get a second monitor for my desk?", "Hardware", "Low"),
    ("My mouse has stopped working even with new batteries.", "Hardware", "Medium"),
    # Software
    ("Excel crashes every time I open large files.", "Software", "Medium"),
    ("Outlook won't open for anyone in the finance team and month-end reports are due today.", "Software", "High"),
    ("Can you install Zoom on my laptop?", "Software", "Low"),
    ("Teams keeps freezing during my calls.", "Software", "Medium"),
    ("The payroll system shows an error and staff won't get paid tomorrow if it isn't fixed.", "Software", "High"),
    ("Word's spell check is set to American English instead of British English.", "Software", "Low"),
    # Account
    ("I forgot my password and I'm locked out of my account.", "Account", "Medium"),
    ("I got a sign-in alert from another country and I think someone else is in my account.", "Account", "High"),
    ("A new starter joins on Monday and needs an email account set up.", "Account", "Low"),
    ("My account got locked after too many login attempts.", "Account", "Medium"),
    ("Please change the display name on my email from Mike to Michael.", "Account", "Low"),
    ("I clicked a link in a suspicious email and typed in my password.", "Account", "High"),
    # Other
    ("Where can I find the IT policy document?", "Other", "Low"),
    ("Who should I talk to about IT training for my team?", "Other", "Low"),
    ("Can IT help us plan the move to the new office next month?", "Other", "Low"),
    ("I'd like to suggest a new project management tool. Who do I speak to?", "Other", "Low"),
    ("What are the IT support desk's opening hours?", "Other", "Low"),
    ("Can I get a copy of last month's IT support report for my manager?", "Other", "Low"),
]