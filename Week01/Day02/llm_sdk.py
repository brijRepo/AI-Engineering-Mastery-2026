class BaseLLM:
    def __init__(self, model_name):
        self.model_name = model_name

    def connect(self):
        print(f"Connected to {self.model_name}")

    def generate(self, prompt):
        print(f"Generating response for: {prompt}")

    def disconnect(self):
        print(f"Disconnected from {self.model_name}")

class GPTModel(BaseLLM):
    def __init__(self):
        super().__init__("GPT")

    def generate(self, prompt):
        print(f"GPT Response: {prompt}")


class ClaudeModel(BaseLLM):
    def __init__(self):
        super().__init__("Claude")

    def generate(self, prompt):
        print(f"Claude Response: {prompt}")


class GeminiModel(BaseLLM):
    def __init__(self):
        super().__init__("Gemini")

    def generate(self, prompt):
        print(f"Gemini Response: {prompt}")

gpt = GPTModel()

gpt.connect()
gpt.generate("Hello")
gpt.disconnect()