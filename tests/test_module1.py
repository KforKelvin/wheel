import unittest
from my_package.module1 import hello

class TestModule1(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()