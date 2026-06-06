import unittest

from textconverter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestTextConverter(unittest.TestCase):
    def test_bold_conversion(self):
        node = TextNode("This is a text with a **bold** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertTrue(isinstance(new_nodes, list))
        self.assertTrue(isinstance(new_nodes[0], TextNode))
        self.assertEqual(new_nodes[0].text, "This is a text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertTrue(isinstance(new_nodes[1], TextNode))
        self.assertEqual(new_nodes[1].text, "bold")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertTrue(isinstance(new_nodes[2], TextNode))
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)

    def test_italic_conversion(self):
        node = TextNode("This is a text with a _italic_ word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertTrue(isinstance(new_nodes, list))
        self.assertTrue(isinstance(new_nodes[0], TextNode))
        self.assertEqual(new_nodes[0].text, "This is a text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertTrue(isinstance(new_nodes[1], TextNode))
        self.assertEqual(new_nodes[1].text, "italic")
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)
        self.assertTrue(isinstance(new_nodes[2], TextNode))
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)

    def test_code_conversion(self):
        node = TextNode("This is a text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertTrue(isinstance(new_nodes, list))
        self.assertTrue(isinstance(new_nodes[0], TextNode))
        self.assertEqual(new_nodes[0].text, "This is a text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertTrue(isinstance(new_nodes[1], TextNode))
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertTrue(isinstance(new_nodes[2], TextNode))
        self.assertEqual(new_nodes[2].text, " word")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)

    def test_mulitple_conversion(self):
        node = TextNode(
            "This is a text with a `code block`, a **bold** word and an _italic_ word",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        new_nodes = split_nodes_delimiter([*new_nodes], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter([*new_nodes], "_", TextType.ITALIC)
        self.assertTrue(isinstance(new_nodes, list))
        self.assertTrue(isinstance(new_nodes[0], TextNode))
        self.assertEqual(new_nodes[0].text, "This is a text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertTrue(isinstance(new_nodes[1], TextNode))
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertTrue(isinstance(new_nodes[2], TextNode))
        self.assertEqual(new_nodes[2].text, ", a ")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)
        self.assertTrue(isinstance(new_nodes[3], TextNode))
        self.assertEqual(new_nodes[3].text, "bold")
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)
        self.assertTrue(isinstance(new_nodes[4], TextNode))
        self.assertEqual(new_nodes[4].text, " word and an ")
        self.assertEqual(new_nodes[4].text_type, TextType.PLAIN)
        self.assertTrue(isinstance(new_nodes[5], TextNode))
        self.assertEqual(new_nodes[5].text, "italic")
        self.assertEqual(new_nodes[5].text_type, TextType.ITALIC)
        self.assertTrue(isinstance(new_nodes[6], TextNode))
        self.assertEqual(new_nodes[6].text, " word")
        self.assertEqual(new_nodes[6].text_type, TextType.PLAIN)

    def test_mulitple_conversion_out_of_order(self):
        node = TextNode(
            "This is a text with a `code block`, a **bold** word and an _italic_ word",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter([*new_nodes], "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter([*new_nodes], "`", TextType.CODE)
        self.assertTrue(isinstance(new_nodes, list))
        self.assertTrue(isinstance(new_nodes[0], TextNode))
        self.assertEqual(new_nodes[0].text, "This is a text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertTrue(isinstance(new_nodes[1], TextNode))
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertTrue(isinstance(new_nodes[2], TextNode))
        self.assertEqual(new_nodes[2].text, ", a ")
        self.assertEqual(new_nodes[2].text_type, TextType.PLAIN)
        self.assertTrue(isinstance(new_nodes[3], TextNode))
        self.assertEqual(new_nodes[3].text, "bold")
        self.assertEqual(new_nodes[3].text_type, TextType.BOLD)
        self.assertTrue(isinstance(new_nodes[4], TextNode))
        self.assertEqual(new_nodes[4].text, " word and an ")
        self.assertEqual(new_nodes[4].text_type, TextType.PLAIN)
        self.assertTrue(isinstance(new_nodes[5], TextNode))
        self.assertEqual(new_nodes[5].text, "italic")
        self.assertEqual(new_nodes[5].text_type, TextType.ITALIC)
        self.assertTrue(isinstance(new_nodes[6], TextNode))
        self.assertEqual(new_nodes[6].text, " word")
        self.assertEqual(new_nodes[6].text_type, TextType.PLAIN)
