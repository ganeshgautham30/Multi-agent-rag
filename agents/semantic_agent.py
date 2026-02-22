from difflib import get_close_matches

def fuzzy_resolve(value: str, choices):
    matches = get_close_matches(value, list(choices), n=1, cutoff=0.6)
    return matches[0] if matches else value