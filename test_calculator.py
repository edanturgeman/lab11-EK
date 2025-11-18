import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
         self.assertEqual(add(1, 2), 3)
         self.assertEqual(add(55, 20), 75)
         self.assertEqual(add(35, 80), 115)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(300, 50), 250)
        self.assertEqual(subtract(55, 20), 35)
        self.assertEqual(subtract(60, 20), 40)
    # ##########################

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(mul(2,4), 8)
        self.assertEqual(mul(5,2),10)
        self.assertEqual(mul(7,5), 35)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2,10),5)
        self.assertEqual(div(5,25),5)
        self.assertEqual(div(10,60),6)
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
        self.assertEqual(logarithm(1,10),0)
        self.assertEqual(logarithm(10,10),1)
        self.assertEqual(logarithm(100,10),2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
             logarithm(0, "a")

    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm("x",10)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(math.hypot(3,4),5 )
        self.assertEqual(math.hypot(5,12),13)
        self.assertEqual(math.hypot(8,15),17)


    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root("a")
        with self.assertRaises(ValueError):
            square_root(-5)
        self.assertEqual(square_root(4), 2)





    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()