import pandas as pd
# Load dataset once at module level
df = pd.read_csv("data/interviewtestdataset.csv")

def run_structured_query(entities: dict):
   # Work on copy
   result = df.copy()
   # -----------------------------
   # Chemical Name Filter
   # -----------------------------
   chemical_value = entities.get("ChemicalName", "")
   if chemical_value:
       if "ChemicalName" in result.columns:
           result = result[
               result["ChemicalName"]
               .astype(str)
               .str.contains(chemical_value, case=False, na=False)
           ]
   # -----------------------------
   # Brand Name Filter
   # -----------------------------
   brand_value = entities.get("BrandName", "")
   if brand_value:
       if "BrandName" in result.columns:
           result = result[
               result["BrandName"]
               .astype(str)
               .str.contains(brand_value, case=False, na=False)
           ]
   # -----------------------------
   # CAS Number Filter
   # -----------------------------
   cas_value = entities.get("CasNumber", "")
   if cas_value:
       if "CasNumber" in result.columns:
           result = result[
               result["CasNumber"]
               .astype(str)
               .str.contains(cas_value, case=False, na=False)
           ]
   # -----------------------------
   # Year Filter
   # -----------------------------
   year_value = entities.get("Year", "")
   if year_value:
       # Case 1: If dataset has DiscontinuedDate column
       if "DiscontinuedDate" in result.columns:
           result = result[
               result["DiscontinuedDate"]
               .astype(str)
               .str.contains(year_value, na=False)
           ]
       # Case 2: If dataset has explicit Year column
       elif "Year" in result.columns:
           result = result[
               result["Year"]
               .astype(str)
               .str.contains(year_value, na=False)
           ]
   return result