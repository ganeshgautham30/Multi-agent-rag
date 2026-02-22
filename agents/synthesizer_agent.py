def synthesize_answer(question: str, df_result, plan_steps):
    if df_result.empty:
        return {
            "status": "No Matching Records",
            "answer": "No matching records found for the given query.",
            "details": [],
            "query_plan": plan_steps
        }

    # Short Answer
    short_answer = f"{len(df_result)} matching products found for the query."

    # Detailed Evidence (citations)
    details = []
    for _, row in df_result.head(5).iterrows():
        details.append({
            "ProductName": row.get("ProductName"),
            "CompanyName": row.get("CompanyName"),
            "BrandName": row.get("BrandName"),
            "ChemicalName": row.get("ChemicalName"),
            "CasNumber": row.get("CasNumber")
        })

    return {
        "status": "Exact Match Found",
        "answer": short_answer,
        "details": details,
        "query_plan": plan_steps
    }