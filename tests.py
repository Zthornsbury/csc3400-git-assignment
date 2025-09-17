from calculator import add, subtract, multiply, divide, power, square_root

   def test_add():
       assert add(2, 3) == 5
       assert add(-1, 1) == 0
       print("Add tests passed")

   def test_subtract():
       assert subtract(5, 3) == 2
       assert subtract(0, 5) == -5
       print("Subtract tests passed")

   def test_multiply():
       assert multiply(4, 3) == 12
       assert multiply(-2, 3) == -6
       print("Multiply tests passed")

   def test_divide():
       assert divide(10, 2) == 5
       assert divide(7, 2) == 3.5
       print("Divide tests passed")

   def test_power():
       assert power(2, 3) == 8
       assert power(5, 0) == 1
       print("Power tests passed")

   def test_square_root():
       assert square_root(9) == 3
       assert square_root(16) == 4
       print("Square root tests passed")

   if __name__ == "__main__":
       test_add()
       test_subtract()
       test_multiply()
       test_divide()
       test_power()
       test_square_root()
       print("All tests passed!")