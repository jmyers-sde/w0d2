# test_main.py

import unittest
from main import hello_world

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Welcome to Git!")

if __name__ == '__main__':
    unittest.main()



from main import greet_person

class TestHelloWorld(unittest.TestCase):
    def test_greet_person(self):
        self.assertEqual(greet_person(), "Hello, Susan!")

if __name__ == '__second__':
    unittest.main() 