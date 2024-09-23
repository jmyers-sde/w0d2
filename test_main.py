# test_main.py

import unittest
from main import hello_world
from main import greet_person

class TestHelloWorld(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello from Justin Myers!")

if __name__ == '__main__':
    unittest.main()


class TestHelloWorld(unittest.TestCase):
    def test_greet_person(self):
        response = greet_person("Susan")
        self.assertTrue(type(response))

if __name__ == '__second__':
    unittest.main() 