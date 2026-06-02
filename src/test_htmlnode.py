import unittest

from htmlnode import HTMLNode, LeafNode


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
        self.assertEqual(
            repr(node), "HTMLNode(p, This is a paragraph, children: None, None)"
        )


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(), '<a href="https://www.google.com">Click me!</a>'
        )

    def test_leaf_to_html_raw_text(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_value_is_none(self):
        node = LeafNode("div", "dummy")
        node.value = None
        with self.assertRaises(
            ValueError,
        ):
            node.to_html()

    def test_repr(self):
        node = LeafNode(tag="p", value="This is a paragraph")
        self.assertEqual(repr(node), "LeafNode(p, This is a paragraph, None)")


if __name__ == "__main__":
    unittest.main()
