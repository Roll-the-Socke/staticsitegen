import unittest
from markdowntransformation import *
from textnode import *
from htmlnode import *

class TestSplitting(unittest.TestCase):
        
    def test_basic(self):
        node = TextNode("Hello **world** today", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text, "Hello ")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[1].text, "world")
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(new_nodes[2].text, " today")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_no_delimiters(self):
        node = TextNode("Hello world today", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text, "Hello world today")
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_split_nodes_delimiter_invalid(self):
        node = TextNode("Hello **world today", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(str(context.exception), "Not a valid Markdown Text")

if __name__ == "__main__":
    unittest.main()