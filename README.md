# Multi-Agent Orchestrator RAG System

## Project Overview
This project is a basic implementation of a Multi-Agent Retrieval-Augmented Generation (RAG) system built on top of the Chemical Disclosure dataset.  
The goal is to answer user queries by extracting relevant entities, applying structured filtering on the dataset, and returning grounded responses with supporting evidence.

The system is intentionally designed in a modular way so that each responsibility is handled by a separate agent. This makes the flow easy to understand, test, and extend later with more advanced models or vector search.

## How the System Works
When a user asks a question, the following steps happen:

1. The Planner Agent first checks the type of question (lookup, date filter, etc.)
2. The Entity Extraction Agent pulls out key filters like Chemical Name, Brand, CAS Number, or Year
3. The Structured Query Agent applies those filters directly on the dataset using pandas
4. The Semantic Agent (basic fuzzy matching) helps handle slight variations in entity names
5. The Answer Synthesizer Agent converts the retrieved rows into a short answer along with detailed evidence
6. Finally, the Orchestrator Agent coordinates all steps and returns the final response

This ensures that every answer is based only on actual dataset records and not on assumptions.

## Output Format
For each query, the system returns:
- Status (for example: Exact Match Found or No Matching Records)
- A short natural language answer
- Detailed evidence rows from the dataset
- A query plan trace showing how the answer was derived

This makes the system transparent and easy to debug.

---

## Project Structure
multi_agent_rag/
├── main.py
├── agents/
│ ├── planner_agent.py
│ ├── entity_agent.py
│ ├── sql_agent.py
│ ├── semantic_agent.py
│ ├── synthesizer_agent.py
│ └── orchestrator.py
└── data/
└── interviewtestdataset.csv

---

Each agent has a single clear responsibility, which keeps the design clean and easy to follow.

---

## How to Run
1. Create a virtual environment:
   python -m venv venv

2. Activate it:
   venv\Scripts\activate

3. Install required packages:
   pip install pandas python-dateutil

4. Run the application:
   python main.py

---

## Example Questions to Try
- Which products contain Chemical Titanium Dioxide?
- Show products discontinued in 2024 with Chemical Paraben
- Which products contain CAS 75-07-0?
- What chemicals are reported for Brand LOREAL?

---

## Notes
This is a rule-based baseline implementation meant to demonstrate the orchestration logic and explainability.  
The same architecture can later be extended with vector databases or LLM-based agents for more advanced reasoning.

The main focus of this project is clarity, modular design, and grounded answers with traceable evidence.

