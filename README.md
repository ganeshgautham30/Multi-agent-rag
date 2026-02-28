# Multi-Agent Chemical Disclosure Assistant
## Overview
This project implements a modular Multi-Agent Retrieval and Reasoning system for querying a structured cosmetic chemical disclosure dataset using natural language.
The system converts user queries into structured filters, executes deterministic dataset queries, and optionally enhances results using LLM-based semantic reasoning.
The architecture follows a clear separation of concerns:
- Intent Planning
- Entity Extraction
- Structured Data Retrieval
- Optional Semantic Refinement
- Final Response Synthesis
This ensures explainability, modularity, and scalability.
---
## Problem Statement
Users should be able to ask natural language questions such as:
- Show products for brand AVON
- List chemicals used in 2023
- Find products containing Benzene
- Show all products for CAS number 50-00-0
The system must:
1. Understand user intent
2. Extract structured entities
3. Perform deterministic dataset filtering
4. Optionally refine results using semantic reasoning
5. Return structured and explainable output
---
## System Architecture
User Query
   │
   ▼
Planner Agent (Intent Classification)
   │
   ▼
Entity Agent (Entity Extraction)
   │
   ▼
SQL Agent (Structured Filtering - Pandas)
   │
   ├── If Results Found
   │        ▼
   │   Semantic Agent (LLM Reasoning)
   │
   ▼
Synthesizer Agent (Final Response Builder)
   │
   ▼
User Output
---
## Component Responsibilities
### Planner Agent
- Classifies user intent
- Determines execution path
- Routes query within orchestration layer
### Entity Agent
Extracts structured fields from natural language:
- ChemicalName
- BrandName
- CompanyName
- CasNumber
- Year
Returns a dictionary used for structured filtering.
### SQL Agent
Performs deterministic filtering using Pandas.
Key characteristics:
- Case-insensitive matching
- Safe handling of missing values
- Conditional filtering based on extracted entities
- Returns filtered DataFrame
Ensures accuracy and prevents hallucination.
### Semantic Agent (Optional Layer)
Enhances structured results using a local LLM (via Ollama).
Responsibilities:
- Context-aware reasoning over filtered rows
- Summarizing structured results
- Providing analytical insights
This layer operates only after deterministic filtering to maintain grounding.
### Synthesizer Agent
Formats final output including:
- Status
- Answer summary
- Query plan trace
- Optional semantic explanation
Ensures transparency of execution.
---
## Execution Flow
1. User enters query in CLI
2. Orchestrator receives request
3. Planner classifies intent
4. Entity Agent extracts structured fields
5. SQL Agent performs dataset filtering
6. Optional Semantic Agent refines results
7. Synthesizer prepares final response
8. Output returned to user
---
## Project Structure
multi_agent_rag/
│
├── agents/
│   ├── planner_agent.py
│   ├── entity_agent.py
│   ├── sql_agent.py
│   ├── semantic_agent.py
│   └── synthesizer_agent.py
│
├── core/
│   ├── llm_client.py
│
├── data/
│   └── interviewtestdataset.csv
│
├── orchestrator.py
├── main.py
├── requirements.txt
└── README.md
---
## Setup and Installation
### 1. Clone Repository
git clone https://github.com/ganeshgautham30/multi-agent-rag.git
cd multi-agent-rag
### 2. Create Virtual Environment
Windows:
python -m venv venv
venv\Scripts\activate
Mac/Linux:
python3 -m venv venv
source venv/bin/activate
### 3. Install Dependencies
pip install -r requirements.txt
requirements.txt should contain:
pandas
requests
### 4. Install and Start Ollama (Required for Semantic Layer)
Download Ollama from:
https://ollama.com
Pull model:
ollama pull mistral
Start server:
ollama serve
Ensure it runs on:
http://localhost:11434
---
## Running the Application
After activating the virtual environment:
python main.py
You will see:
Type your question below. Type 'exit' to quit.
---
## Example Queries
- show products for brand AVON
- show products discontinued in 2018
- find products containing Titanium Dioxide
- how many products are there for brand AVON
- show products for brand AVON discontinued in 2018 that contain Titanium Dioxide
---
## Design Principles
- Deterministic structured filtering first
- Optional LLM reasoning second
- Clear separation of responsibilities
- Modular multi-agent orchestration
- Transparent query plan tracing
---
## Future Improvements
- Aggregation and trend-based queries
- REST API interface
- Frontend UI integration
- Docker-based deployment
- Vector-based semantic retrieval
   

 
 
