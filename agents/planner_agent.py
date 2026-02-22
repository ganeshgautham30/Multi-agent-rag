def classify_intent(question: str) -> str:
    q = question.lower()

    if "trend" in q or "over time" in q:
        return "trend"
    elif "discontinued" in q or "removed" in q:
        return "date_filter"
    elif "compare" in q:
        return "compare"
    elif "summarize" in q or "summary" in q:
        return "summary"
    else:
        return "lookup"