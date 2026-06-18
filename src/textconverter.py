import re
from typing import Text

from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        split_nodes = []
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(parts)):
            if parts[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(parts[i], TextType.PLAIN))
            else:
                split_nodes.append(TextNode(parts[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text: str) -> list[tuple[str, str]]:
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text: str) -> list[tuple[str, str]]:
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        text_to_split = node.text
        images = extract_markdown_images(node.text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image_alt, image_link in images:
            parts = text_to_split.split(f"![{image_alt}]({image_link})", maxsplit=1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.PLAIN))
            new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
            text_to_split = parts[1]
        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, TextType.PLAIN))
    return new_nodes


def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue
        text_to_split = node.text
        links = extract_markdown_links(node.text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link_text, link_url in links:
            parts = text_to_split.split(f"[{link_text}]({link_url})", maxsplit=1)
            if len(parts) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.PLAIN))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            text_to_split = parts[1]
        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, TextType.PLAIN))
    return new_nodes


if __name__ == "__main__":
    node = TextNode(
        "This is a text with a `code block`, a **bold** word and an _italic_ word",
        TextType.PLAIN,
    )
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter([*new_nodes], "`", TextType.CODE)
    new_nodes = split_nodes_delimiter([*new_nodes], "**", TextType.BOLD)
    print(f"Example output of 'split_nodes_delimiter' for {node}:")
    print(new_nodes)
    print()

    images = extract_markdown_images(
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    )
    print("Example output of 'extract_markdown_images':")
    print(images)
    print()

    links = extract_markdown_links(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    )
    print("Example output of 'extract_markdown_links':")
    print(links)
    print()

    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.PLAIN,
    )
    new_nodes = split_nodes_image([node])
    print(f"Example output of 'split_nodes_image' for {node}:")
    print(new_nodes)
    print()

    node = TextNode(
        "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.PLAIN,
    )
    new_nodes = split_nodes_link([node])
    print(f"Example output of 'split_nodes_link' for {node}:")
    print(new_nodes)
