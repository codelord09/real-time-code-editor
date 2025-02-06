import requests

DEEPSEEK_API_KEY = "DEEPSEEK_API_KEY"
DEEPSEEK_API_URL = "https://api.deepseek.com/v1/completions"


def get_debugging_suggestions(code: str):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "deepseek-r1",
        "prompt": f"Debug the following code:\n{code}",
        "max_tokens": 100,
    }
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json().get("choices")[0].get("text").strip()
    else:
        raise Exception(f"Error calling DeepSeek API: {response.text}")
