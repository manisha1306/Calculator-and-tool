import unittest
from calculator import *

def setUpModule():
    print('Start the testing module')

def tearDownModule():
    print('End the testing module')

class TestCalculator(unittest.TestCase):

   @classmethod
   def setUpClass(self):
      print('Set up class')
      self.calc = Calculator()

   def test_add(self):
      self.assertEqual(self.calc.add(2, 7), 9, msg=None)
      self.assertEqual(self.calc.add(-5, 5), 0, msg=None)
      self.assertEqual(self.calc.add(-7, -5), -12, msg=None)

   def test_subtract(self):
      self.assertEqual(self.calc.subtract(2, 7), -5, msg=None)
      self.assertEqual(self.calc.subtract(-5, 6), -11, msg=None)
      self.assertEqual(self.calc.subtract(7, -5), 12, msg=None)

   def test_multiply(self):
      self.assertEqual(self.calc.multiply(2, 7), 14, msg=None)
      self.assertEqual(self.calc.multiply(-5, 6), -30, msg=None) 
      self.assertEqual(self.calc.multiply(-1, 1), -1, msg=None)
      self.assertEqual(self.calc.multiply(-1, -1), 1, msg=None)  

   def test_divide(self):
      
      self.assertEqual(self.calc.divide(10, 5), 2, msg=None)
      self.assertEqual(self.calc.divide(-1, 1), -1, msg=None)
      self.assertEqual(self.calc.divide(-1, -1), 1, msg=None)
      self.assertEqual(self.calc.divide(5, 2), 2.5, msg=None)

   def test_interger_divide(self):
      
      self.assertEqual(self.calc.integer_divide(10, 5), 2, msg=None)
      self.assertEqual(self.calc.integer_divide(-1, 1), -1, msg=None)
      self.assertEqual(self.calc.integer_divide(-1, -1), 1, msg=None)
      self.assertEqual(self.calc.integer_divide(5, 2), 2, msg=None)  

   def test_power(self):
      
      self.assertEqual(self.calc.power(10, 2), 100, msg=None)
      self.assertEqual(self.calc.power(-1, 1), -1, msg=None)
      self.assertEqual(self.calc.power(2, -2), 0.25, msg=None)

   def test_square(self):
      
      self.assertEqual(self.calc.square(10), 100, msg=None)
      self.assertEqual(self.calc.square(-6), 36, msg=None)

   def test_root(self):
      
      self.assertEqual(self.calc.root(16), 4, msg=None)
      self.assertEqual(self.calc.root(25), 5, msg=None)
      self.assertEqual(self.calc.root(625), 25, msg=None)

   def test_factorial(self):
      
      self.assertEqual(self.calc.factorial(1258623), 1, msg=None)
      self.assertEqual(self.calc.factorial(0), 1, msg=None)
      self.assertEqual(self.calc.factorial(5), 120, msg=None)

if __name__ == '__main__':
   unittest.main()

   

