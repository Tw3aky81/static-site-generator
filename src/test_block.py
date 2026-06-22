import unittest

from block import BlockType, block_to_block_type, makdown_to_blocks


class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = makdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_with_extra_spaces_and_newline_removed(self):
        md = """
This is **bolded** paragraph      


       This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line


      


- This is a list
- with items
"""
        blocks = makdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_paragraph_blocktype(self):
        block = "This is an ordinary paragraph block"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.PARAGRAPH_TYPE)

    def test_block_to_heading_blocktype(self):
        block = "# This is a heading 1"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.HEADING_TYPE)

    def test_block_to_code_blocktype(self):
        block = "```\nThis is a multiline\ncode block\nwith code\n```"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.CODE_TYPE)

    def test_block_to_quote_blocktype(self):
        block = (
            "> This is a multiline\n>quote block\n> with optional spaces after bracket"
        )
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.QUOTE_TYPE)

    def test_block_to_ul_blocktype(self):
        block = "- This is a multiline\n- unordered list block\n- with items"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.UL_TYPE)

    def test_block_to_ol_blocktype(self):
        block = "1. This is a multiline\n2. ordered list block\n3. with items"
        blocktype = block_to_block_type(block)
        self.assertEqual(blocktype, BlockType.OL_TYPE)
