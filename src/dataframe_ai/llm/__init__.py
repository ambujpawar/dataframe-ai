"""
The base class implementation for all LLMs.
"""


class LLM:
    """
    The base class implementation for all LLMs.
    """

    def generate_code(self, query) -> str:
        """
        Generates the code for the given query.

        :param query: The query to generate code for.
        :return: The generated code.
        """
        raise NotImplementedError("Method not implemented")

    def get_code_block(self, response) -> str:
        """
        Parses the response from the LLM and returns the code block

        :param response: The query to get code for.
        :return: The code.
        """
        raise NotImplementedError("Method not implemented")
