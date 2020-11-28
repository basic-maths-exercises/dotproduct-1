import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_function_exists(self) : 
        self.assertTrue( "dotProduct" in globals(), "No function called dotProduct has been declared" )
        
    def test_function_correct(self) : 
        for i in range(1,10) :
            x1 = np.zeros(i)
            x2 = np.zeros(i)
            dp = 0 
            for j in range(i) : 
                x1[j], x2[j]  = np.random.uniform(-1,1), np.random.uniform(-1,1)
                dp = dp + x1[j]*x2[j]
            self.assertTrue( np.abs(dotProduct( x1, x2) - dp)<1e-7, "The dot product function does not work" )
