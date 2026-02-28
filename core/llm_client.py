import requests
OLLAMA_URL = "http://localhost:11434/api/generate"
def call_llm(prompt: str) -> str:
   try:
       response = requests.post(
           OLLAMA_URL,
           json={
               "model": "mistral",
               "prompt": prompt,
               "stream": False
           },
           timeout=60  # important!
       )
       response.raise_for_status()
       return response.json().get("response", "")
   except requests.exceptions.Timeout:
       return "LLM Error: Request timed out."
   except Exception as e:
       return f"LLM Error: {str(e)}"