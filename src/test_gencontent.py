import unittest
from gencontent import extract_title  # adjust the import based on where your function is

class TestExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"  # what's a simple h1 markdown?
        
        # act: call the function
        result = extract_title(markdown)
        
        # assert: check the result
        self.assertEqual(result, "Hello")


if __name__ == "__main__":
    unittest.main()
