from core.ai_planner import AIPlanner
from core.tool_manager import ToolManager
from ai.provider import get_provider


class Brain:

    def __init__(self):

        self.planner = AIPlanner()
        self.tools = ToolManager()
        self.ai = get_provider()

    def think(self, message):

        plan = self.planner.decide(message)

        steps = plan.get("steps", [])

        # Normal conversation
        if not steps:
            return self.ai.chat(message)

        results = []

        for step in steps:

            tool_name = step.get("tool")
            args = step.get("args", {})

            if not tool_name:
                continue

            print()
            print("Executing:", tool_name)
            print("Arguments:", args)

            try:

                result = self.tools.execute(
                    tool_name,
                    **args
                )

                print("Result:", result)

                if tool_name == "read_file":

                    if result:
                        results.append(result)
                    else:
                        results.append("Unable to read the file.")

                elif result:

                    results.append(
                        f"{tool_name} completed successfully."
                    )

                else:

                    results.append(
                        f"{tool_name} failed."
                    )

            except Exception as e:

                error = f"Tool Error: {e}"

                print(error)

                results.append(error)

                break

        if not results:

            return "I could not complete that task."

        return "\n".join(results)