import openai

openai.api_key = "your-openai-api-key"

def summarize_alert(log: str) -> str:
    prompt = f"""
    Summarize the following log in human-readable format:
    {log}
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response['choices'][0]['message']['content'].strip()
