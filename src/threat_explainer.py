import openai

def explain_threat(log: str, question: str) -> str:
    prompt = f"""
    Log:
    {log}

    Question:
    {question}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200
    )
    return response['choices'][0]['message']['content'].strip()
