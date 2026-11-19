import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "Explain Java in simple words",
    "stream": False
}

response = requests.post(url, json=data)
response = response.json()

print(response["response"])