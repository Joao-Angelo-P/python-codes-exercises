from fatorials import *
import unittest

expected = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
class TestFatorial(unittest.TestCase):
    def test_fatorial1(self):
        for i in range(11):
            self.assertEqual(fatorial_1(i), expected[i])
            
    def test_fatorial2(self):
        for i in range(11):
            self.assertEqual(fatorial_2(i), expected[i])
            
    def test_fatorial3(self):
        for i in range(11):
            self.assertEqual(fatorial_3(i), expected[i])
            
    def test_fatorial4(self):
        for i in range(11):
            self.assertEqual(fatorial_4(i), expected[i])

if __name__ == '__main__':
    unittest.main()
