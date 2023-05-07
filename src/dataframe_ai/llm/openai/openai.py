"""
Implement OpenAI's API
"""
import os
from typing import Optional

# Third-party imports
import openai
from dotenv import load_dotenv

# Local imports
from dataframe_ai.llm import LLM

load_dotenv()


class OpenAI(LLM):
    """
    dataframe_ai wrapper for OpenAI's LLMs
    """

    api_key: str
    model: str = "gpt-3.5-turbo-0301"
    temperature: float = 0.0
    max_tokens: int = 512
    top_p: float = 1.0
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
    stop: Optional[str] = None

    def __init__(self, api_key: str, **kwargs):
        """
        Initialize the OpenAI LLM.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("API key not provided")

        openai.api_key = self.api_key
        self._set_parameters(**kwargs)

    def _set_parameters(self, **kwargs):
        """
        Set the parameters for the LLM.
        """
        valid_params = [
            "model",
            "temperature",
            "max_tokens",
            "top_p",
            "frequency_penalty",
            "presence_penalty",
            "stop",
        ]
        for key, value in kwargs.items():
            if key in valid_params:
                setattr(self, key, value)
            else:
                raise ValueError(f"Invalid parameter {key}")
