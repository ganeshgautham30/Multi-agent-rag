import re

def extract_entities(question: str) -> dict:
    entities = {}

    chem = re.search(r'chemical\s+([\w\s\-]+)', question, re.IGNORECASE)
    if chem:
        entities["ChemicalName"] = chem.group(1).strip()

    brand = re.search(r'brand\s+([\w\s\-]+)', question, re.IGNORECASE)
    if brand:
        entities["BrandName"] = brand.group(1).strip()

    cas = re.search(r'cas\s*([\d\-]+)', question, re.IGNORECASE)
    if cas:
        entities["CasNumber"] = cas.group(1).strip()

    year = re.search(r'(20\d{2})', question)
    if year:
        entities["Year"] = year.group(1)

    return entities