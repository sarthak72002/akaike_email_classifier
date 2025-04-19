import spacy
import subprocess
import sys
import re

# Load SpaCy Model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run([sys.executable, "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Define regex patterns
patterns = {
    "email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "phone_number": r"(\+91[\-\s]?)?[0]?[6789]\d{9}",
    "dob": r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
    "aadhar_num": r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3,4}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/\d{2,4}\b"
}

def mask_text(text):
    masked_text = text
    entities = []
    already_masked = set()

    for label, pattern in patterns.items():
        for match in re.finditer(pattern, masked_text):
            start, end = match.span()
            original = match.group()

            if (start, end) in already_masked:
                continue

            masked_label = f"[{label}]"
            masked_text = masked_text[:start] + masked_label + masked_text[end:]
            entities.append({
                "position": [start, end],
                "classification": label,
                "entity": original
            })
            already_masked.add((start, end))

    doc = nlp(masked_text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            start, end = ent.start_char, ent.end_char
            original = ent.text
            masked_label = "[full_name]"
            masked_text = masked_text[:start] + masked_label + masked_text[end:]
            entities.append({
                "position": [start, end],
                "classification": "full_name",
                "entity": original
            })

    return masked_text, entities


