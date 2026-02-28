from orchestrator import run_orchestrator

def main():
   print("\n=== Multi-Agent Chemical Disclosure Assistant ===")
   print("Type your question below. Type 'exit' to quit.\n")
   while True:
       question = input("Ask: ")
       if question.lower() in ["exit", "quit"]:
           print("Goodbye")
           break
       response = run_orchestrator(question)
       print("\n--- STATUS ---")
       print(response.get("status"))
       print("\n--- ANSWER ---")
       print(response.get("answer"))
       print("\n--- QUERY PLAN ---")
       for step in response.get("query_plan", []):
           print("•", step)
       if "semantic_analysis" in response:
           print("\n--- SEMANTIC ANALYSIS ---")
           print(response["semantic_analysis"])
       print("\n" + "="*50 + "\n")

if __name__ == "__main__":
   main()