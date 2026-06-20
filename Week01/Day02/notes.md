# Class
groups related data (attributes) and functions (methods) into a single package

Example:
class Car:
    def __init__(self, brand):
        self.brand = brand                  # Attribute
    def drive(self):                        # Method
        return f"The {self.brand} is now driving."

AI Usage:
Everything is built using classes. Frameworks like PyTorch, TensorFlow, and Hugging Face rely entirely on classes to build, train, and deploy AI models.


# Object
Instance of a class.

Example:
car1 = Car("Tesla", "Model 3")              # Object
print(car1.brand)

AI Usage:
You create and manipulate AI Objects to load models, process data, and generate predictions.

#Constructor
A special method inside a class that automatically runs whenever you create a new object.

Example:
def __init__(self, brand):                  # Constructor
        self.brand = brand                  

AI Usage:
Hyperparameter Setup in Machine Learning Models, Model Initialisation and Weight Seeding (Deep Learning),
Managing API Clients and Sessions (GenAI / LLMs), etc.


# Method
A funtion that belongs to an object.

Example:
class Car:
    def __init__(self, brand):
        self.brand = brand
    def drive(self):                        # Method
        return f"The {self.brand} is now driving."

AI Usage:
Train networks, clean data, generate predictions

# Inheritnce
A concept of OOP that allows a new class to adopt the attributes and methods of an existing class.

Example:
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some generic sound"

class Dog(Animal):
    def speak(self):  # Overriding the parent method
        return "Woof!"

my_dog = Dog("Buddy")
print(my_dog.name)   # Inherited attribute -> Output: Buddy
print(my_dog.speak())  # Overridden method -> Output: Woof!

AI Usage:
In frameworks like PyTorch and Tensorflown, inheritance is used constantly. We almost never write a neural network from scratch.


SOLID PRINCIPLES:

# Single Responsibility Principle
A class should have only one reason to change.

Example:
#BAD: Class handles both data fetching and formatting
class ReportManager:
    def fetch_data(self): pass
    def format_to_html(self): pass

#GOOD: Split into two dedicated classes
class DataFetcher:
    def fetch(self): pass

class HTMLFormatter:
    def format(self, data): pass

AI Usage:
In AI pipelines, you separate Data Preprocessing from Model Training. You do not write tokenisation, image resizing, and gradient updates inside a single class


# Open/Closed Principle
Software entities should be open for extension, but closed for modification.

Example:
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self): return self.w * self.h

#Extension: Adding a Circle requires zero changes to the Rectangle class
class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

AI Usage:
AI deployment frameworks like Hugging Face Transformers or LangChain rely heavily on OCP. If you want to add a custom LLM provider or a new neural network architecture, you do not modify the core library source code.


# Liskov Substitution Principle
Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.

Example:
class Bird:
    def fly(self): return "Flying high"

#BAD: Ostrich breaks LSP because it cannot fly!
class Ostrich(Bird):
    def fly(self): raise NotImplementedError("Can't fly")

#GOOD: Refactor the hierarchy
class Bird: pass
class FlyingBird(Bird):
    def fly(self): return "Flying high"
class Ostrich(Bird): pass

AI Usage:
In Scikit-Learn, every model (like LinearRegression, RandomForestClassifier, or SVC) inherits from base estimator classes. Because they strictly follow LSP, you can swap out LinearRegression for a complex GradientBoostingRegressor in your pipeline code seamlessly. Both guarantee they implement .fit(X, y) and .predict(X) without breaking your downstream evaluation system.


# Interface Segregation Principle
Clients should not be forced to depend on methods they do not use.

Example:
from abc import ABC, abstractmethod

#BAD: A fat interface forcing all workers to implement everything
class MultiWorker(ABC):
    @abstractmethod
    def code(self): pass
    @abstractmethod
    def design(self): pass

#GOOD: Segregated, granular classes
class Codeable(ABC):
    @abstractmethod
    def code(self): pass

class Designable(ABC):
    @abstractmethod
    def design(self): pass

AI Usage:
In AI cloud production (like AWS SDK or MLflow), logging metrics is decoupled from saving massive model artifacts. An automated hyperparameter optimization script might only need an interface to write small float metrics (LogMetricsInterface) but shouldn't be forced to implement file upload streams (SaveArtifactsInterface) which require complex cloud storage configurations.


# Dependency Inversion Principle
High-level modules should not depend on low-level modules. Both should depend on abstractions.

Example:
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data): pass

class MySQLDatabase(Database):
    def save(self, data): print("Saved to MySQL")

#High-level class depends on the abstraction (Database), not the concrete MySQL class
class UserRegistration:
    def __init__(self, db: Database):
        self.db = db

AI Usage:
When deploying an AI chatbot production system, your orchestrator system shouldn't rigidly depend directly on the OpenAI_API_Client class. Instead, it depends on a generic LLMClient abstraction. This lets you swap the backend from OpenAI to a locally hosted Llama model or Anthropic's Claude instantly by simply changing the injected configuration, without rewriting a single line of your core chatbot application logic.
