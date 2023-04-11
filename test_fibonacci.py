import unittest

from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test1(self):
        self.assertEqual(1,fibonacci(1))
    def test2(self):
        self.assertEqual(1,fibonacci(2))
    def test3(self):
        self.assertEqual(2,fibonacci(3))
    def test4(self):
        self.assertEqual(3,fibonacci(4))
    def test5(self):
        self.assertEqual(5,fibonacci(5))


if __name__=="__main__":
    unittest.main() 