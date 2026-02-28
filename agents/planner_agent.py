from core.llm_client import call_llm

def classify_intent(question: str) -> str:
    prompt = f"""
you are intent clasiification agent.

classify the following query into one of:

-structured_lookup
-hybrid_query
-trend_analysis
-summary
-compare

Query: {question}

Return ONLY the category name.
"""
    response = call_llm(prompt).strip().lower()

    if "structured" in response:
        return "structured_lookup"
    if "hybrid" in response:
        return "hybrid_query"
    if "trend" in response:
        return "trend_analysis"
    if "summary" in response:
        return "summary"
    if "compare" in response:
        return "compare"
    

    return "structured_lookup"