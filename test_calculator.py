import unittest
from calculator import *

#https://github.com/edanturgeman/lab11-EK
#Partner 1: Edan Turgeman
#Partner 2: Kevin Taing

class TestCalculator(unittest.TestCase):
     def test_add(self):
         self.assertEqual(add(1, 2), 3)
         self.assertEqual(add(55, 20), 75)
         self.assertEqual(add(35, 80), 115)

     def test_subtract(self): # 3 assertions
        self.assertEqual(sub(300, 50), 250)
        self.assertEqual(sub(55, 20), 35)
        self.assertEqual(sub(60, 20), 40)
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
     def test_divide_by_zero(self): # 1 assertion

         with self.assertRaises(ZeroDivisionError):
             div(0, 5)
         # call division function inside, example:
         # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)

     def test_logarithm(self): # 3 assertions
         self.assertEqual(log(1,10),0)
         self.assertEqual(log(10,10),1)
         self.assertEqual(log(100,10),2)

     def test_log_invalid_base(self): # 1 assertion
         with self.assertRaises(ValueError):
             log(0, "a")
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()