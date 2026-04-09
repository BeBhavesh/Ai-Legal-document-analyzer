import re

def analyze_text(text):

    # Simple summary (first few lines)
    summary = " ".join(text.split()[:80])

    # Keyword detection
    risks = []
    keywords = ["penalty", "termination", "breach", "liability", "fine"]

    for word in keywords:
        if word.lower() in text.lower():
            risks.append(word)

    return f"""
Summary:
{summary}

Key Clauses:
- Payment Terms
- Termination Clause
- Liability Clause

Risk Factors:
{', '.join(risks) if risks else 'No major risks detected'}
"""