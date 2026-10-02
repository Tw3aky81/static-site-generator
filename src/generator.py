def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("Error: Markdown contains no h1 header")


if __name__ == "__main__":
    md = """
# Hello
"""
    title = extract_title(md)
    print(title)
