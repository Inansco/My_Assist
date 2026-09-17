import re


class Planner:
    def __init__(self):
        pass

    def decide(self, message: str):

        text = message.strip()

        lower = text.lower()

        # ------------------------
        # OPEN APPLICATION
        # ------------------------

        if lower.startswith("open "):

            app = text[5:].strip()

            return {
                "tool": "open_app",
                "args": {
                    "name": app
                }
            }

        # ------------------------
        # CLOSE APPLICATION
        # ------------------------

        if lower.startswith("close "):

            app = text[6:].strip()

            return {
                "tool": "close_app",
                "args": {
                    "name": app
                }
            }

        # ------------------------
        # CREATE FOLDER
        # ------------------------

        if lower.startswith("create folder "):

            path = text[len("create folder "):].strip()

            return {
                "tool": "create_folder",
                "args": {
                    "path": path
                }
            }

        # ------------------------
        # CREATE FILE
        # ------------------------

        if lower.startswith("create file "):

            path = text[len("create file "):].strip()

            return {
                "tool": "create_file",
                "args": {
                    "path": path
                }
            }

        # ------------------------
        # READ FILE
        # ------------------------

        if lower.startswith("read file "):

            path = text[len("read file "):].strip()

            return {
                "tool": "read_file",
                "args": {
                    "path": path
                }
            }

        # ------------------------
        # WRITE FILE
        # Format:
        #
        # write file C:\temp\hello.txt | Hello World
        #
        # ------------------------

        if lower.startswith("write file "):

            command = text[len("write file "):]

            parts = command.split("|", 1)

            if len(parts) == 2:

                return {
                    "tool": "write_file",
                    "args": {
                        "path": parts[0].strip(),
                        "content": parts[1].strip()
                    }
                }

        # ------------------------
        # No tool found
        # ------------------------

        return {
            "tool": None,
            "args": {}
        }