import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_HTMLNode(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)

    def test_HTMLNode_with_data(self):
        node = HTMLNode(tag="p", value="This is a paragraph")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_props_to_html(self):
        props = {
            "href": "https://www.boot.dev",
            "target": "_blank",
        }
        node = HTMLNode(props=props)
        self.assertEqual(
            ' href="https://www.boot.dev" target="_blank"', node.props_to_html()
        )

    def test_repr(self):
        node = HTMLNode(tag="p", value="This is a paragraph")
        self.assertEqual(repr(node), "HTMLNode(p, This is a paragraph, None, None)")


if __name__ == "__main__":
    unittest.main()
