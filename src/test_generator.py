import unittest

from generator import extract_title


class TestGenerator(unittest.TestCase):
    def test_extract_title(self):
        md = "# Hello"
        title = extract_title(md)
        self.assertEqual(title, "Hello")

    def test_extract_no_title(self):
        md = "Hello"
        self.assertRaises(ValueError, extract_title, md)
