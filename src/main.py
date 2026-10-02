import os
import shutil

from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType


def main() -> None:
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    static_dir = os.path.abspath(os.path.join(project_root, "static"))
    dest_dir = os.path.abspath(os.path.join(project_root, "public"))

    if not os.path.exists(static_dir):
        raise ValueError("Error: Directory 'static' does not exist.")
    elif os.path.isfile(static_dir):
        raise ValueError("Error: Directory 'static' is not a directory.")

    stage_directory(dest_dir)
    copy_recursively(static_dir, dest_dir)


def stage_directory(dest: str) -> None:
    if not os.path.exists(dest):
        os.mkdir(dest, 0o755)
        print(f"Created directory {dest}")
    elif os.path.isfile(dest):
        raise ValueError("Error: Destination is not a directory.")
    else:
        shutil.rmtree(dest)
        os.mkdir(dest, 0o755)
        print(f"Cleared directory {dest}")


def copy_recursively(from_dir: str, to_dir: str) -> None:
    items = os.listdir(from_dir)
    for item in items:
        item_path = os.path.abspath(os.path.join(from_dir, item))
        if os.path.isfile(item_path):
            shutil.copy(item_path, to_dir)
            print(f"Copied '{item}' to {to_dir}")
        else:
            new_dir = os.path.abspath(os.path.join(to_dir, item))
            os.mkdir(new_dir, 0o755)
            print(f"Created directory {new_dir}")
            copy_recursively(item_path, new_dir)


if __name__ == "__main__":
    main()
