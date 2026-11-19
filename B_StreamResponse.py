from ollama import chat

response = chat(
    model="llama3.2",
    messages=[
        {
            "role": "user",
            "content": "what is python"
        }
    ],
    stream=True
)

for chunk in response:
    print(chunk.message.content, end="", flush=True)