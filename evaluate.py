from triage import triage_ticket
from eval_data import TEST_TICKETS


def main():
    total = len(TEST_TICKETS)
    category_correct = 0
    priority_correct = 0
    mistakes = []

    for number, (text, expected_category, expected_priority) in enumerate(TEST_TICKETS, start=1):
        try:
            result = triage_ticket(text)
            got_category = result["category"]
            got_priority = result["priority"]
        except Exception:
            got_category = "ERROR"
            got_priority = "ERROR"

        if got_category == expected_category:
            category_correct += 1
        if got_priority == expected_priority:
            priority_correct += 1
        if got_category != expected_category or got_priority != expected_priority:
            mistakes.append((text, expected_category, got_category, expected_priority, got_priority))

        print(f"{number}/{total} checked")

    print()
    print(f"Category accuracy: {category_correct}/{total} = {category_correct / total:.0%}")
    print(f"Priority accuracy: {priority_correct}/{total} = {priority_correct / total:.0%}")

    if mistakes:
        print("\nWhere the AI disagreed:")
        for text, exp_cat, got_cat, exp_pri, got_pri in mistakes:
            print(f"- {text}")
            print(f"    category: expected {exp_cat}, got {got_cat}")
            print(f"    priority: expected {exp_pri}, got {got_pri}")


if __name__ == "__main__":
    main()