"""
Inansco Configuration
"""

# ----------------------------
# AI
# ----------------------------

AI_NAME = "Inansco"

AI_PROVIDER = "test"

OLLAMA_HOST = "http://localhost:11434"

OLLAMA_MODEL = "llama3.2:1b"

SYSTEM_PROMPT = """
You are Inansco.

You are a personal AI assistant created by Efada Monday.

Your personality:
- Friendly
- Intelligent
- Professional
- Helpful

Never claim you completed an action unless a tool confirms it.

Keep answers concise unless the user asks for details.
"""

# ----------------------------
# Go Engine
# ----------------------------

GO_ENGINE_URL = "http://localhost:8081"

# ----------------------------
# Voice
# ----------------------------

WAKE_WORD = "Hey Inansco"

VOICE_ENABLED = False

# ----------------------------
# Logging
# ----------------------------

DEBUG = True