from openai import OpenAI
from dotenv import load_dotenv
import os

import config


load_dotenv()


class OpenAIProvider:

    def __init__(self):

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY is not configured")

        self.client = OpenAI(api_key=api_key)

    def chat(self, message: str):

        response = self.client.responses.create(
            model="gpt-5.6-luna",
            instructions=config.SYSTEM_PROMPT,
            input=message,
        )

        return response.output_text