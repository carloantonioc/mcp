# test_n8n.py
import requests

TOKEN = "Aqui tu Token"  # con sk-
URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

data = {
    "model": "qwen-turbo",
    "messages": [{"role": "user", "content": "Hola"}],
    "max_tokens": 10
}

resp = requests.post(URL, headers=headers, json=data)
print("Status:", resp.status_code)
print("Respuesta:", resp.text)