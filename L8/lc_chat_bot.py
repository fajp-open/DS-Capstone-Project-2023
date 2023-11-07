
import random


class ChatBotStatic:
    """
    Static ChatBot
    """

    def __init__(self):
        self.memory = []

    def generate_response(self, message: str):
        """
        Returns a static response
        """
        return "How can I help you?"


class ChatBotRandom:
    """
    Static ChatBot
    """

    def __init__(self):
        self.memory = []

    def generate_response(self, message: str):
        """
        Returns a static response
        """
        return random.choice(
            [
                "Hello there! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need help?",
            ]
        )
