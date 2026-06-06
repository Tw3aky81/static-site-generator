from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
        else:
            parts = node.text.split(delimiter)
            for i in range(len(parts)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(parts[i], TextType.PLAIN))
                else:
                    new_nodes.append(TextNode(parts[i], text_type))

    return new_nodes


if __name__ == "__main__":
    node = TextNode(
        "This is a text with a `code block`, a **bold** word and an _italic_ word",
        TextType.PLAIN,
    )
    new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
    new_nodes = split_nodes_delimiter([*new_nodes], "`", TextType.CODE)
    new_nodes = split_nodes_delimiter([*new_nodes], "**", TextType.BOLD)
    print(new_nodes)
