import json

from ai.ollama_provider import OllamaProvider


class AIPlanner:

    def __init__(self):
        self.ai = OllamaProvider()

    def decide(self, message):

        prompt = f"""
You are the task planner for Inansco.

Available tools:

open_app(name)
close_app(name)
create_folder(path)
create_file(path)
write_file(path, content)
read_file(path)

Convert the user's request into a sequence of tool calls.

Return ONLY valid JSON.

Example:

{{
    "steps": [
        {{
            "tool": "create_folder",
            "args": {{
                "path": "C:\\\\Users\\\\monda\\\\Desktop\\\\TestAI"
            }}
        }},
        {{
            "tool": "create_file",
            "args": {{
                "path": "C:\\\\Users\\\\monda\\\\Desktop\\\\TestAI\\\\hello.txt"
            }}
        }},
        {{
            "tool": "write_file",
            "args": {{
                "path": "C:\\\\Users\\\\monda\\\\Desktop\\\\TestAI\\\\hello.txt",
                "content": "Hello Monday"
            }}
        }},
        {{
            "tool": "read_file",
            "args": {{
                "path": "C:\\\\Users\\\\monda\\\\Desktop\\\\TestAI\\\\hello.txt"
            }}
        }}
    ]
}}

If no tool is required, return:

{{
    "steps": []
}}

Rules:

- Return JSON only.
- Do not use Markdown.
- Do not explain anything.
- Use only the six available tools.
- Keep actions in the correct order.
- Preserve the user's requested file content.
- Preserve paths exactly when supplied.

User request:

{message}
"""

        response = self.ai.chat(prompt)

        try:
            return json.loads(response)

        except json.JSONDecodeError:

            print("Planner returned invalid JSON:")
            print(response)

            return {
                "steps": []
            }