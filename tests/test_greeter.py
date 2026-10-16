import unittest

from greeter import farewell, greet, load_config


class GreetTest(unittest.TestCase):
    def test_default(self):
        self.assertEqual(greet("Ada", {}), "Hello, Ada.")

    def test_excited(self):
        self.assertEqual(greet("Ada", {"greeting": "Hi", "excited": True}), "Hi, Ada!")

    def test_config_file(self):
        config = load_config("config/greeter.json")
        self.assertEqual(greet("Ada", config), "Welcome, Ada!")

    def test_farewell(self):
        self.assertEqual(farewell("Ada", {"excited": True}), "Goodbye, Ada!")
        self.assertEqual(farewell("Ada", {}), "Goodbye, Ada.")


if __name__ == "__main__":
    unittest.main()
