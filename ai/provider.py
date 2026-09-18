import config

from ai.test_provider import TestProvider
from ai.openai_provider import OpenAIProvider


def get_provider():

    if config.AI_PROVIDER == "openai":
        return OpenAIProvider()

    if config.AI_PROVIDER == "test":
        return TestProvider()

    raise ValueError(
        f"Unknown AI provider: {config.AI_PROVIDER}"
    )