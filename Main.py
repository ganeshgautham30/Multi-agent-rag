from agents.orchestrator import run_orchestrator

def main():
    print("=== Multi-Agent Chemical Disclosure RAG System ===")

    while True:
        question = input("\nAsk your question (type 'exit' to quit): ")
        if question.lower() == "exit":
            break

        response = run_orchestrator(question)

        print("\n===== STATUS =====")
        print(response["status"])

        print("\n===== SHORT ANSWER =====")
        print(response["answer"])

        print("\n===== DETAILED EVIDENCE =====")
        for row in response["details"]:
            print(
                f"Product: {row['ProductName']} | "
                f"Company: {row['CompanyName']} | "
                f"Brand: {row['BrandName']} | "
                f"Chemical: {row['ChemicalName']} | "
                f"CAS: {row['CasNumber']}"
            )

        print("\n===== QUERY PLAN TRACE =====")
        for step in response["query_plan"]:
            print("-", step)

if __name__ == "__main__":
    main()