from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


def main() -> None:
    tn = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(tn)

    hn = HTMLNode("h1", "This is header 1", props={"target": "_self"})
    print(hn)

    pn = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "Italic text"),
            LeafNode(None, "Normal text"),
        ],
        {"class": "AlertRed"},
    )
    print(pn)


if __name__ == "__main__":
    main()
