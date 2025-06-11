import openai

def suggest_remediation(log: str) -> str:
    prompt = f"""
    Given this log:

    {log}
    Suggest a remediation step.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response['choices'][0]['message']['content'].strip()
