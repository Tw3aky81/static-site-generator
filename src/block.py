from enum import Enum
import re

from htmlnode import HTMLNode, ParentNode
from inline import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


class BlockType(Enum):
    PARAGRAPH_TYPE = "paragraph"
    HEADING_TYPE = "heading"
    CODE_TYPE = "code"
    QUOTE_TYPE = "quote"
    UL_TYPE = "unordered_list"
    OL_TYPE = "ordered_list"


def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    block_nodes: list[HTMLNode] = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING_TYPE:
            block_nodes.append(create_heading_node(block))
        elif block_type == BlockType.PARAGRAPH_TYPE:
            block_nodes.append(create_paragraph_node(block))
        elif block_type == BlockType.QUOTE_TYPE:
            block_nodes.append(create_quote_node(block))
        elif block_type == BlockType.OL_TYPE:
            block_nodes.append(create_ol_node(block))
        elif block_type == BlockType.UL_TYPE:
            block_nodes.append(create_ul_node(block))
        elif block_type == BlockType.CODE_TYPE:
            block_nodes.append(create_code_node(block))
        else:
            raise ValueError("Error: Unknown block type encountered in markdown")

    root = ParentNode("div", block_nodes)
    return root


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    raw_blocks = markdown.split("\n\n")
    for block in raw_blocks:
        block = block.strip()
        if block != "":
            blocks.append(block)
    return blocks


# Lane did it with plain if else then and for loop logic.
# I want to see how my regex solution turns out.
def block_to_block_type(block: str) -> BlockType:
    if re.search(r"^#{1,6} .+$", block):
        return BlockType.HEADING_TYPE
    if re.search(r"^`{3}\n[\S\s]+`{3}$", block, re.MULTILINE):
        return BlockType.CODE_TYPE
    if re.search(r"^> ?.+$", block, re.MULTILINE):
        return BlockType.QUOTE_TYPE
    if re.search(r"^- .+$", block, re.MULTILINE):
        return BlockType.UL_TYPE
    if re.search(r"^\d\. .+$", block, re.MULTILINE):
        return BlockType.OL_TYPE
    return BlockType.PARAGRAPH_TYPE


def text_to_children(text: str) -> list[HTMLNode]:
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes


def create_heading_node(block: str) -> ParentNode:
    children = text_to_children(block)
    node = ParentNode("h1", children)
    return node


def create_paragraph_node(block: str) -> ParentNode:
    children = text_to_children(block.replace("\n", " "))
    node = ParentNode("p", children)
    return node


def create_quote_node(block: str) -> ParentNode:
    children = text_to_children(block)
    node = ParentNode("blockquote", children)
    return node


def create_ul_node(block: str) -> ParentNode:
    children = text_to_children(block)
    node = ParentNode("ul", children)
    return node


def create_ol_node(block: str) -> ParentNode:
    children = text_to_children(block)
    node = ParentNode("ol", children)
    return node


def create_code_node(block: str) -> ParentNode:
    text = repr(block.strip("```").strip()).strip("'").strip('"')
    text_node = TextNode(text, TextType.CODE)
    children = text_node_to_html_node(text_node)
    node = ParentNode("pre", [children])
    return node


if __name__ == "__main__":
    md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)
