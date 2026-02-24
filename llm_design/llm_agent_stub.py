"""
This file is a simple demonstration of how LLM calls can be integrated
into the existing multi-agent pipeline.

Right now the project uses rule-based logic, but this shows where and how
an LLM (like OpenAI or any agent framework) could be plugged in later.
"""


def call_llm(prompt: str) -> str:
    """
    This function simulates an LLM call.
    In a real system, this would call an API like OpenAI or Azure OpenAI.
    For now, we just print the prompt and return a mock response.
    """
    print("\n--- LLM CALL ---")
    print("Prompt:")
    print(prompt)
    print("--- END OF PROMPT ---\n")

    # returning a dummy response just for demonstration
    return "mock_llm_response"


def planner_llm(user_query: str):
    """
    Example: how planner agent could use an LLM to classify intent.
    """
    prompt = f"""
You are a planning agent for a chemical disclosure query system.
Classify the intent of the following user query into one of these:
lookup, date_filter, summary, trend.

User Query: {user_query}

Return only the intent label.
"""
    return call_llm(prompt)


def entity_extraction_llm(user_query: str):
    """
    Example: how entity extraction could be done using an LLM.
    """
    prompt = f"""
Extract the following entities from the query if present:
- ChemicalName
- BrandName
- CasNumber
- Year

User Query: {user_query}

Return the result in JSON format.
"""
    return call_llm(prompt)


def synthesizer_llm(user_query: str, retrieved_rows):
    """
    Example: how the final response could be generated using LLM
    based only on the retrieved dataset rows.
    """
    prompt = f"""
Generate a concise answer using only the given records.

User Query: {user_query}

Retrieved Records:
{retrieved_rows}

Do not add any extra information not present in the records.
"""
    return call_llm(prompt)


if __name__ == "__main__":
    # simple demo run to show how LLM calls would be triggered
    query = "Which products contain Chemical Titanium Dioxide discontinued in 2024?"

    print("Planner LLM Output:")
    planner_llm(query)

    print("Entity Extraction LLM Output:")
    entity_extraction_llm(query)

    print("Synthesizer LLM Output:")
    synthesizer_llm(query, "sample_rows_here")