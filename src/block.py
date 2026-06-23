from enum import Enum
import re


class BlockType(Enum):
    PARAGRAPH_TYPE = "paragraph"
    HEADING_TYPE = "heading"
    CODE_TYPE = "code"
    QUOTE_TYPE = "quote"
    UL_TYPE = "unordered_list"
    OL_TYPE = "ordered_list"


def makdown_to_blocks(markdown: str) -> list[str]:
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
