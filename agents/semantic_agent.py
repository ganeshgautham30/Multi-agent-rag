from core.llm_client import call_llm

class SemanticAgent:
   def refine_results(self, question: str, df_result):
       # If no results, skip semantic reasoning
       if df_result.empty:
           return None
       # Limit rows to avoid timeout
       top_rows = df_result.head(3)
       # Build lightweight summary instead of full dataframe
       summary = f"""
User Question:
{question}
Total matching rows: {len(df_result)}
Top 3 matching records:
{top_rows[['ProductName', 'BrandName', 'ChemicalName']].to_string(index=False)}
"""
       prompt = f"""
You are a data analysis assistant.
Based on the structured SQL results below,
provide a short, clear summary answering the user question.
Keep it concise.
{summary}
"""
       try:
           response = call_llm(prompt)
           return response
       except Exception as e:
           return f"LLM Error: {str(e)}"