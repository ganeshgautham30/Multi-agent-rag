from agents.planner_agent import classify_intent
from agents.entity_agent import extract_entities
from agents.sql_agent import run_structured_query
from agents.synthesizer_agent import synthesize_answer
from agents.semantic_agent import SemanticAgent

# Initialize Semantic Agent
semantic_agent = SemanticAgent()

def run_orchestrator(question: str):
   plan_steps = []
   # -----------------------------
   # Step 1 — Intent Classification
   # -----------------------------
   intent = classify_intent(question)
   plan_steps.append(f"Intent classified as: {intent}")
   # -----------------------------
   # Step 2 — Entity Extraction
   # -----------------------------
   entities = extract_entities(question)
   plan_steps.append(f"Extracted entities: {entities}")
   print("DEBUG ENTITIES", entities)
   # -----------------------------
   # Step 3 — Structured Retrieval
   # -----------------------------
   df_result = run_structured_query(entities)
   plan_steps.append("Executed structured SQL query")
   # -----------------------------
   # Step 4 — Semantic Reasoning
   # -----------------------------
   semantic_analysis = None
   if not df_result.empty and len(df_result) < 50:
       semantic_analysis = semantic_agent.refine_results(
           question,
           df_result
       )
       plan_steps.append("Executed LLM-based semantic reasoning")
   # -----------------------------
   # Step 5 — Final Synthesis
   # -----------------------------
   response = synthesize_answer(
       question,
       df_result,
       plan_steps
   )
   # Attach semantic explanation if available
   if semantic_analysis:
       response["semantic_analysis"] = semantic_analysis
   return response