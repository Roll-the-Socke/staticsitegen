import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_text(self):
        node = TextNode("Ich gehe zur Schule", TextType.ITALIC)
        node2 = TextNode("Ich gehe zur Uni", TextType.ITALIC)
        self.assertEqual(node, node2)
    
    def test_type(self):
        node = TextNode("Ich gehe arbeiten", TextType.BOLD)
        node2 = TextNode("Ich gehe arbeiten", TextType.ITALIC)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("Ich gehe bowlen", TextType.BOLD, "google.com")
        node2 = TextNode("Ich gehe bowlen", TextType.BOLD)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
