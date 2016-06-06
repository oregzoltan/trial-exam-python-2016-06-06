import unittest
from greet import greeter

class TestGreeter(unittest.TestCase):

    def test_zoli(self):
        self.assertEqual(greeter('Zoli'), 'Hello, Zoli!')

    def test_empty_string(self):
        self.assertEqual(greeter(''), 'Hello, Mr Nobody!')

    # def test_is_vovel_a(self):
    #     self.assertTrue(extend.is_vovel('a'))

if __name__ == '__main__':
    unittest.main()
