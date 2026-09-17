import requests
import config


class ToolManager:
    def __init__(self):
        self.base_url = config.GO_ENGINE_URL
        self.tools = {}

        # Register built-in tools
        self.register("open_app", self.open_app)
        self.register("close_app", self.close_app)
        self.register("create_folder", self.create_folder)
        self.register("create_file", self.create_file)
        self.register("write_file", self.write_file)
        self.register("read_file", self.read_file)

    # -------------------------
    # Tool Registry
    # -------------------------

    def register(self, name, func):
        self.tools[name] = func

    def execute(self, tool_name, **kwargs):
        tool = self.tools.get(tool_name)

        if tool is None:
            raise ValueError(f"Unknown tool: {tool_name}")

        return tool(**kwargs)

    # -------------------------
    # Applications
    # -------------------------

    def open_app(self, name):

        response = requests.post(
            f"{self.base_url}/apps/open",
            json={
                "name": name
            }
        )

        return response.status_code == 200

    def close_app(self, name):

        response = requests.post(
            f"{self.base_url}/apps/close",
            json={
                "name": name
            }
        )

        return response.status_code == 200

    # -------------------------
    # Files
    # -------------------------

    def create_folder(self, path):

        response = requests.post(
            f"{self.base_url}/files/create-folder",
            json={
                "path": path
            }
        )

        return response.status_code == 200

    def create_file(self, path):

        response = requests.post(
            f"{self.base_url}/files/create-file",
            json={
                "path": path
            }
        )

        return response.status_code == 200

    def write_file(self, path, content):

        response = requests.post(
            f"{self.base_url}/files/write",
            json={
                "path": path,
                "content": content
            }
        )

        return response.status_code == 200

    def read_file(self, path):

        response = requests.post(
            f"{self.base_url}/files/read",
            json={
                "path": path
            }
        )

        if response.status_code == 200:
            return response.text

        return None