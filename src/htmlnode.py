class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:
        fmt_string = ""
        if self.props:
            for k, v in self.props.items():
                fmt_string += f' {k}="{v}"'
        return fmt_string

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(
        self, tag: str | None, value: str, props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, value, props=props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
