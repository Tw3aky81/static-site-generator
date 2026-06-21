def makdown_to_blocks(markdown: str) -> list[str]:
    blocks = []
    raw_blocks = markdown.split("\n\n")
    for block in raw_blocks:
        block = block.strip()
        if block != "":
            blocks.append(block)
    return blocks
