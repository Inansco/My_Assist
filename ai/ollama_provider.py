from ollama import Client
import config


class OllamaProvider:
    def __init__(self):
        self.client = Client(host=config.OLLAMA_HOST)

    def chat(self, message: str):

        response = self.client.chat(
            model=config.OLLAMA_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": config.SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )

        return response["message"]["content"]