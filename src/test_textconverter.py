from typing import Text
import unittest

from textconverter import (
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)
from textnode import TextNode, TextType

""" Tests are not incorrect, but the solution uses assertListEqual.
    TODO: rewrite with assertListEqual"""


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

    def test__conversion_invalid_doc(self):
        node = TextNode(
            "This is a text with a `code block`, a **bold word and an _italic_ word",
            TextType.PLAIN,
        )
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test__conversion_empty_tag(self):
        node = TextNode("This is a text with a **** word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertTrue(isinstance(new_nodes, list))
        self.assertTrue(isinstance(new_nodes[0], TextNode))
        self.assertEqual(new_nodes[0].text, "This is a text with a ")
        self.assertEqual(new_nodes[0].text_type, TextType.PLAIN)
        self.assertTrue(isinstance(new_nodes[1], TextNode))
        self.assertEqual(new_nodes[1].text, " word")
        self.assertEqual(new_nodes[1].text_type, TextType.PLAIN)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_multiple_images(self):
        matches = extract_markdown_images(
            "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        )
        self.assertListEqual(
            [
                ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
                ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"),
            ],
            matches,
        )

    def test_extract_markdown_no_images(self):
        matches = extract_markdown_images("This is text with no images")
        self.assertListEqual([], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link to boot.dev](https://www.boot.dev)"
        )
        self.assertListEqual([("link to boot.dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_multiple_links(self):
        matches = extract_markdown_links(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        )
        self.assertListEqual(
            [
                ("to boot dev", "https://www.boot.dev"),
                ("to youtube", "https://www.youtube.com/@bootdotdev"),
            ],
            matches,
        )

    def test_extract_markdown_no_links(self):
        matches = extract_markdown_links("This is text with no links")
        self.assertListEqual([], matches)

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.PLAIN),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_no_images(self):
        node = TextNode(
            "This is text with an fake image and another dummy",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode(
                    "This is text with an fake image and another dummy", TextType.PLAIN
                ),
            ],
            new_nodes,
        )

    def test_split_only_images(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png) ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" ", TextType.PLAIN),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_only_one_images(self):
        node = TextNode(
            "![image](https://i.imgur.com/zjjcJKZ.png)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.PLAIN),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.PLAIN),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_no_links(self):
        node = TextNode(
            "This is text with a fake link",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a fake link", TextType.PLAIN),
            ],
            new_nodes,
        )

    def test_split_only_links(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev) [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" ", TextType.PLAIN),
                TextNode(
                    "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                ),
            ],
            new_nodes,
        )

    def test_split_only_one_links(self):
        node = TextNode(
            "[to boot dev](https://www.boot.dev)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            ],
            new_nodes,
        )
