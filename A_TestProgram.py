from ollama import chat

response = chat(
    model = "llama3.2",
    messages =[
        {
            "role":"user",
            "content":"what is python"
        }
    ],
    stream = False
)

print("response====>",response.message.content)

