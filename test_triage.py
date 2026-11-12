import pytest
from triage import parse_response


def test_clean_json_is_parsed():
    raw = '{"category": "Network", "priority": "High", "summary": "No Wi-Fi.", "reply": "Hi"}'
    result = parse_response(raw)
    assert result["category"] == "Network"
    assert result["priority"] == "High"


def test_extra_text_around_json_is_ignored():
    raw = 'Sure! Here you go: {"category": "Account", "priority": "Low", "summary": "x", "reply": "y"} Hope that helps.'
    result = parse_response(raw)
    assert result["category"] == "Account"


def test_unknown_category_becomes_other():
    raw = '{"category": "Printer", "priority": "High", "summary": "x", "reply": "y"}'
    assert parse_response(raw)["category"] == "Other"


def test_unknown_priority_becomes_medium():
    raw = '{"category": "Hardware", "priority": "Urgent", "summary": "x", "reply": "y"}'
    assert parse_response(raw)["priority"] == "Medium"


def test_missing_fields_are_filled_in():
    raw = '{"category": "Software", "priority": "Low"}'
    result = parse_response(raw)
    assert result["summary"] == ""
    assert result["reply"] == ""


def test_no_json_raises_error():
    with pytest.raises(ValueError):
        parse_response("Sorry, I can't help with that.")