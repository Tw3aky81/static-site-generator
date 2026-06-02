from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main() -> None:
    tn = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    print(tn)

    hn = HTMLNode("h1", "This is header 1", props={"target": "_self"})
    print(hn)


if __name__ == "__main__":
    main()
