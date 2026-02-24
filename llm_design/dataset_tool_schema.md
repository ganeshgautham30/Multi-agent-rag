# Dataset Transformation for Tool-Based LLM Calls

## Overview
The chemical disclosure dataset is currently stored as a CSV file and queried using deterministic pandas filters in the baseline implementation.  
For an LLM-augmented agent system, the dataset needs to be exposed as a structured “data tool” so that an LLM can call it using specific arguments instead of directly writing queries.

The idea is to transform natural language constraints into structured tool parameters that can be safely executed against the dataset.

---

## Tool Definition
The dataset can be exposed as a callable query tool with the following interface:

get_products(
    chemical_name: str | None,
    brand_name: str | None,
    cas_number: str | None,
    year: int | None
) -> List[ProductRecord]

This tool retrieves matching product disclosure records based on the provided filters.

---

## Input Mapping
User queries are first processed by the entity extraction agent, which extracts structured entities.  
These extracted entities are then mapped to tool arguments as shown below:

| Extracted Entity | Tool Argument |
|------------------|--------------|
| ChemicalName     | chemical_name |
| BrandName        | brand_name |
| CasNumber        | cas_number |
| Year constraint  | year |

### Example
User Query:  
“Which products contain Chemical Titanium Dioxide discontinued in 2024?”

Mapped Tool Call:
get_products(
    chemical_name="Titanium Dioxide",
    brand_name=None,
    cas_number=None,
    year=2024
)

This mapping mirrors the current pandas filtering logic implemented in the structured query agent.

---

## Output Schema
Each returned record from the tool follows a structured schema:

ProductRecord = {
    ProductName: str,
    CompanyName: str,
    BrandName: str,
    ChemicalName: str,
    CasNumber: str,
    PrimaryCategory: str,
    SubCategory: str,
    InitialDateReported: str,
    DiscontinuedDate: str
}

This structured output allows the answer synthesis agent (or an LLM) to generate grounded responses using only retrieved dataset records.

---

## Purpose in LLM Agent Flow
In an LLM-driven version of the system, the flow would be:

1. The LLM interprets the user query
2. Structured entities and constraints are extracted
3. The dataset tool (`get_products`) is invoked with those parameters
4. Retrieved records are passed to the synthesis stage to generate the final response

This approach keeps the retrieval deterministic and explainable while enabling the higher-level reasoning to be handled by an LLM agent.

