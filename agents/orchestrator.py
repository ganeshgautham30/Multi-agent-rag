from agents.planner_agent import classify_intent
from agents.entity_agent import extract_entities
from agents.sql_agent import run_structured_query
from agents.synthesizer_agent import synthesize_answer

def run_orchestrator(question: str):
    plan_steps = []

    # Step 1: Intent Classification
    intent = classify_intent(question)
    plan_steps.append(f"Intent classified as: {intent}")

    # Step 2: Entity Extraction
    entities = extract_entities(question)
    plan_steps.append(f"Extracted entities: {entities}")

    # Step 3: Route to Structured Query Agent
    df_result = run_structured_query(entities)
    plan_steps.append("Executed structured query using DataFrame filters")

    # Step 4: Synthesize Final Answer
    response = synthesize_answer(question, df_result, plan_steps)

    return response