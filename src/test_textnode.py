import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode("This is a text node", TextType.LINK)
        node2 = TextNode("This is a different text node", TextType.LINK)
        self.assertNotEqual(node, node2)

    def test_default_url_is_none(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_url_is_not_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        self.assertNotEqual(node.url, None)

    def test_repr(self):
        node = TextNode("This is a test node", TextType.PLAIN, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a test node, text, https://www.boot.dev)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
