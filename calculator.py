# Advanced Mathematical Calculator - Version 1.0
import math

   def add(a, b):
       try:
           if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
               raise TypeError("Arguments must be numbers")
           return a + b
       except Exception as e:
           print(f"Error in addition: {e}")
           raise

   def subtract(a, b):
       try:
           if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
               raise TypeError("Arguments must be numbers")
           return a - b
       except Exception as e:
           print(f"Error in subtraction: {e}")
           raise

   def multiply(a, b):
       try:
           if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
               raise TypeError("Arguments must be numbers")
           return a * b
       except Exception as e:
           print(f"Error in multiplication: {e}")
           raise

   def divide(a, b):
       try:
           if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
               raise TypeError("Arguments must be numbers")
           if b == 0:
               raise ValueError("Cannot divide by zero")
           return a / b
       except Exception as e:
           print(f"Error in division: {e}")
           raise

   def power(base, exponent):
       try:
           if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
               raise TypeError("Arguments must be numbers")
           return base ** exponent
       except Exception as e:
           print(f"Error in power calculation: {e}")
           raise

   def square_root(number):
       try:
           if not isinstance(number, (int, float)):
               raise TypeError("Argument must be a number")
           if number < 0:
               raise ValueError("Cannot calculate square root of negative number")
           return math.sqrt(number)
       except Exception as e:
           print(f"Error in square root calculation: {e}")
           raise

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

