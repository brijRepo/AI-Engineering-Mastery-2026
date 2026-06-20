#Exercise 1:
class Employee:

    def __init__(self, name, email, role):
        self.name = name
        self.email = email
        self.role = role

    def display(self):
        return f"""Name: {self.name}
Email: {self.email}
Role: {self.role}"""

employee1 = Employee("Brijesh", "bk@gmail.com", "Enginner")

# print(f"Employee name is {employee1.name} and his salary is {employee1.salary}")
print(employee1.display())


#Exercise 2:
class LLM:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate(self):
        print(f"Generating response using {self.model_name}")


class GPTModel(LLM):
    def __init__(self):
        super().__init__("GPT")


class ClaudeModel(LLM):
    def __init__(self):
        super().__init__("Claude")


class GeminiModel(LLM):
    def __init__(self):
        super().__init__("Gemini")


gpt = GPTModel()
gpt.generate()


#Exercise 3:
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, engine_object):
        self.engine = engine_object
    def drive(self):
        return self.engine.start()
    
car = Car(Engine())
print(car.drive())