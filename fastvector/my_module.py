# my_module.py

class Calculator:
    def add(self, a, b):
        """Addition method."""
        return a + b

    def subtract(self, a, b):
        """Subtraction method."""
        return a - b

    def multiply(self, a, b):
        """Multiplication method."""
        return a * b

    def divide(self, a, b):
        """Division method."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

class ConditionalProcessor:
    def process(self, x):
        """Process based on different conditions."""
        if x == 1:
            return "Processed for 1"
        elif x == 2:
            return "Processed for 2"
        elif x == 3:
            return "Processed for 3"
        