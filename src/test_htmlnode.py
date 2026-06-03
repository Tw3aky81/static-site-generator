import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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


class TestParentNode(unittest.TestCase):
    def test_parent_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_parent_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

    def test_parent_to_html_with_two_grandchildren(self):
        grandchild_node1 = LeafNode("b", "grandchild1")
        grandchild_node2 = LeafNode("i", "grandchild2")
        child_node = ParentNode("span", [grandchild_node1, grandchild_node2])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><i>grandchild2</i></span></div>",
        )

    def test_parent_to_html_with_two_children(self):
        grandchild_node1 = LeafNode("b", "grandchild1")
        grandchild_node2 = LeafNode("i", "grandchild2")
        grandchild_node3 = LeafNode("b", "grandchild3")
        grandchild_node4 = LeafNode("i", "grandchild4")
        child_node1 = ParentNode("span", [grandchild_node1, grandchild_node2])
        child_node2 = ParentNode("p", [grandchild_node3, grandchild_node4])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><i>grandchild2</i></span><p><b>grandchild3</b><i>grandchild4</i></p></div>",
        )

    def test_parent_to_html_with_children_and_props(self):
        child_node = LeafNode("span", "child", {"class": "quote_span"})
        parent_node = ParentNode("div", [child_node], {"id": "this_id"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="this_id"><span class="quote_span">child</span></div>',
        )

    def test_parent_to_html_children_is_none(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        parent_node.children = None
        self.assertRaises(ValueError, parent_node.to_html)

    def test_parent_to_html_tag_is_none(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        parent_node.tag = None
        self.assertRaises(ValueError, parent_node.to_html)


if __name__ == "__main__":
    unittest.main()
