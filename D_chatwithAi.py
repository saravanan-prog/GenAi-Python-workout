
from ollama import chat

while True:
    question = input("You: ")

    if question.lower() == "exit":
        break

    print("AI: ", end="", flush=True)

    stream = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ],
        stream=True
    )

    for chunk in stream:
        print(chunk.message.content, end="", flush=True)

    print()
