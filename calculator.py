# Advanced Mathematical Calculator
import math

   def power(base, exponent):
       return base ** exponent

   def square_root(number):
       if number < 0:
           raise ValueError("Cannot calculate square root of negative number")
       return math.sqrt(number)

   # Update existing functions with validation
   def add(a, b):
       if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
           raise TypeError("Arguments must be numbers")
       return a + b

   def subtract(a, b):
       if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
           raise TypeError("Arguments must be numbers")
       return a - b

   def multiply(a, b):
       if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
           raise TypeError("Arguments must be numbers")
       return a * b

   def divide(a, b):
       if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
           raise TypeError("Arguments must be numbers")
       if b == 0:
           raise ValueError("Cannot divide by zero")
       return a / b