class TestProvider:

    def chat(self, message: str):

        # Planner simulation
        if "You are the task planner for Inansco" in message:

            user_request = message.split("User request:", 1)[-1].strip()

                # Read file
            if user_request.lower().startswith("read the file "):

                path = user_request[len("read the file "):].strip()

                return (
                    '{"steps": ['
                    '{"tool": "read_file", '
                f'"args": {{"path": "{path}"}}'
                '}]}' 
            )
        
            # Create file + write content
            if user_request.lower().startswith("create a file at ") and " and write " in user_request.lower():

        

                text = user_request[len("create a file at "):]

                path, content = text.split(" and write ", 1)

                content = content.strip()

                if content.lower().endswith(" into it"):
                    content = content[:-len(" into it")].strip()

                return (
                    '{"steps": ['
                    '{"tool": "create_file", '
                    f'"args": {{"path": "{path.strip()}"}}'
                    '},'
                    '{"tool": "write_file", '
                    f'"args": {{"path": "{path.strip()}", "content": "{content}"}}'
                    '}]}' 
                )

            # Create file only
            if user_request.lower().startswith("create a file at "):

                path = user_request[len("create a file at "):].strip()

                return (
                    '{"steps": ['
                    '{"tool": "create_file", '
                    f'"args": {{"path": "{path}"}}'
                    '}]}' 
                )

            return '{"steps": []}'

        # Normal conversation
        return f"Inansco received: {message}"