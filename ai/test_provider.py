class TestProvider:

    def chat(self, message: str):

        if "You are the task planner for Inansco" in message:

            return '{"steps": []}'

        return f"Inansco received: {message}"