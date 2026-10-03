import os

from block import markdown_to_html_node


def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")

    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise ValueError("Error: Markdown contains no h1 header")


def generate_page(from_path: str, template_path: str, dest_path: str) -> None:
    print(f" * {from_path} {template_path} -> {dest_path}")

    content = open(from_path, "r")
    markdown = content.read()
    content.close()

    template = open(template_path, "r")
    html = template.read()
    template.close()

    title = extract_title(markdown)
    content_html = markdown_to_html_node(markdown).to_html()

    html = html.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", content_html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    page = open(dest_path, "w")
    page.write(html)
    page.close()


def generate_pages_recursive(
    dir_path_content: str, template_path: str, dest_dir_path: str
) -> None:
    filenames = os.listdir(dir_path_content)
    for filename in filenames:
        from_filepath = os.path.join(dir_path_content, filename)
        to_filepath = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_filepath) and from_filepath.endswith(".md"):
            html_filename = filename.replace(".md", ".html")
            to_filepath = os.path.join(dest_dir_path, html_filename)
            generate_page(from_filepath, template_path, to_filepath)
        else:
            generate_pages_recursive(from_filepath, template_path, to_filepath)


if __name__ == "__main__":
    md = """
# Hello
"""
    title = extract_title(md)
    print(title)
