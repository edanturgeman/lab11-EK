import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
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
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
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