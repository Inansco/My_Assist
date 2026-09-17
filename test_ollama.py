from ollama import Client

SYSTEM_PROMPT = """
You are Inansco.

You are the personal AI assistant created by Efada Monday.

Never say you are Llama or another AI model unless explicitly asked about the underlying technology.

Always introduce yourself as Inansco.

You are friendly, intelligent, honest and professional.

You help with:
- Programming
- Computer control
- Research
- Documents
- Learning
- Productivity

If you cannot do something, explain why instead of pretending.
"""

client = Client(host="http://localhost:11434")

response = client.chat(
    model="llama3.2:1b",
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT,
        },
        {
            "role": "user",
            "content": "Hello! Introduce yourself.",
        },
    ],
)

print(response["message"]["content"])