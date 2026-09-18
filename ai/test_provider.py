class TestProvider:

    def chat(self, message: str):

        # Planner simulation
        if "You are the task planner for Inansco" in message:

            user_request = message.split("User request:", 1)[-1].strip()

            # --------------------------------
            # Create folder + create file + write
            # --------------------------------

            lower = user_request.lower()

            if (
                lower.startswith("create a folder at ")
                and ", create a file at " in lower
                and " and write " in lower
            ):

                folder_part = user_request[len("Create a folder at "):]

                folder_path, remaining = folder_part.split(
                    ", create a file at ",
                    1
                )

                file_path, content = remaining.split(
                    " and write ",
                    1
                )

                content = content.strip()

                if content.lower().endswith(" into it"):
                    content = content[:-len(" into it")].strip()

                return (
                    '{"steps": ['
                    '{"tool": "create_folder", '
                    f'"args": {{"path": "{folder_path.strip()}"}}'
                    '},'
                    '{"tool": "create_file", '
                    f'"args": {{"path": "{file_path.strip()}"}}'
                    '},'
                    '{"tool": "write_file", '
                    f'"args": {{"path": "{file_path.strip()}", '
                    f'"content": "{content}"}}'
                    '}]}' 
                )

            # --------------------------------
            # Create file + write + read
            # --------------------------------

            if (
                lower.startswith("create a file at ")
                and " and write " in lower
                and ", then read the file " in lower
            ):

                text = user_request[len("create a file at "):]

                file_part, read_part = text.split(
                    ", then read the file ",
                    1
                )

                path, content = file_part.split(
                    " and write ",
                    1
                )

                content = content.strip()

                if content.lower().endswith(" into it"):
                    content = content[:-len(" into it")].strip()

                read_path = read_part.strip()

                return (
                    '{"steps": ['
                    '{"tool": "create_file", '
                    f'"args": {{"path": "{path.strip()}"}}'
                    '},'
                    '{"tool": "write_file", '
                    f'"args": {{"path": "{path.strip()}", '
                    f'"content": "{content}"}}'
                    '},'
                    '{"tool": "read_file", '
                    f'"args": {{"path": "{read_path}"}}'
                    '}]}' 
                )


            # --------------------------------
            # Create file + write
            # --------------------------------

            if (
                lower.startswith("create a file at ")
                and " and write " in lower
            ):

                text = user_request[len("create a file at "):]

                path, content = text.split(
                    " and write ",
                    1
                )

                content = content.strip()

                if content.lower().endswith(" into it"):
                    content = content[:-len(" into it")].strip()

                return (
                    '{"steps": ['
                    '{"tool": "create_file", '
                    f'"args": {{"path": "{path.strip()}"}}'
                    '},'
                    '{"tool": "write_file", '
                    f'"args": {{"path": "{path.strip()}", '
                    f'"content": "{content}"}}'
                    '}]}' 
                )


            # --------------------------------
            # Open application
            # --------------------------------

            if lower.startswith("open "):
            
                name = user_request[len("open "):].strip()

                return (
                    '{"steps": ['
                    '{"tool": "open_app", '
                    f'"args": {{"name": "{name}"}}'
                    '}]}' 
                )


            # --------------------------------
            # Close application
            # --------------------------------
            
            if lower.startswith("close "):
            
                name = user_request[len("close "):].strip()
            
                return (
                    '{"steps": ['
                    '{"tool": "close_app", '
                    f'"args": {{"name": "{name}"}}'
                    '}]}' 
                )



            # --------------------------------
            # Read file
            # --------------------------------

            if lower.startswith("read the file "):

                path = user_request[len("read the file "):].strip()

                return (
                    '{"steps": ['
                    '{"tool": "read_file", '
                    f'"args": {{"path": "{path}"}}'
                    '}]}' 
                )

            # --------------------------------
            # Create folder
            # --------------------------------

            if lower.startswith("create a folder at "):

                path = user_request[len("create a folder at "):].strip()

                return (
                    '{"steps": ['
                    '{"tool": "create_folder", '
                    f'"args": {{"path": "{path}"}}'
                    '}]}' 
                )

            # --------------------------------
            # Create file
            # --------------------------------

            if lower.startswith("create a file at "):

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