"""
Utility functions for the application
"""

import math
from datetime import datetime

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}! Welcome to our team project."

def add_numbers(a, b):
    """Add two numbers"""
    return a + b

def multiply_numbers(a, b):
    """Multiply two numbers"""
    return a * b

def calculate_average(numbers):
    """Calculate average of a list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def get_current_time():
    """Get current time formatted"""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def fibonacci(n):
    """Calculate fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
