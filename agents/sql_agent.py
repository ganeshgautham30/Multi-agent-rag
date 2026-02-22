import pandas as pd
# Load dataset (simple relative path)
df = pd.read_csv("data/interviewtestdataset.csv")

def run_structured_query(entities: dict):
    result = df.copy()

    # Filter by Chemical Name
    if "ChemicalName" in entities:
        result = result[result["ChemicalName"].str.contains(
            entities["ChemicalName"], case=False, na=False)]

    # Filter by Brand Name
    if "BrandName" in entities:
        result = result[result["BrandName"].str.contains(
            entities["BrandName"], case=False, na=False)]

    # Filter by CAS Number
    if "CasNumber" in entities:
        result = result[result["CasNumber"].astype(str).str.contains(
            entities["CasNumber"])]

    # Filter by Year (Discontinued)
    if "Year" in entities:
        result = result[result["DiscontinuedDate"].astype(str).str.contains(
            entities["Year"])]

    return result