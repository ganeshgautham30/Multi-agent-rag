import json
from core.llm_client import call_llm
def extract_entities(question: str) -> dict:
   prompt = f"""
You are an entity extraction system.
Extract the following fields from the user question.
Return ONLY valid JSON.
Do NOT add explanation.
If a field is not present, return empty string "".
Required keys:
- ChemicalName
- BrandName
- CasNumber
- Year
Question:
{question}
Example output:
{{
 "ChemicalName": "",
 "BrandName": "",
 "CasNumber": "",
 "Year": ""
}}
"""
   response = call_llm(prompt)
   try:
       entities = json.loads(response)
   except:
       # fallback safe default
       entities = {
           "ChemicalName": "",
           "BrandName": "",
           "CasNumber": "",
           "Year": ""
       }
   return entities