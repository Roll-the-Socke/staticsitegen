import unittest
from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("a", "Click me!", None, {"href": "https://boot.dev"})
        assert node.props_to_html() == ' href="https://boot.dev"'

    def test_propsnone(self):
        node = HTMLNode("a", "Click me!", None, None)
        assert node.props_to_html() == ""

    def test_propsempty(self):
        node = HTMLNode("a", "Click me!", None, {})
        assert node.props_to_html() == ""

    def test_multiprops(self):
        node = HTMLNode("a", "Click me!", None, {
            "href": "https://boot.dev",
            "class": "button",
            "id": "submit"
        })
        result = node.props_to_html()
    # Check that each attribute is present in the result
        self.assertIn(' href="https://boot.dev"', result)
        self.assertIn(' class="button"', result)
        self.assertIn(' id="submit"', result)
    # Check that the total number of attributes is correct
    # Each attribute starts with a space, so count the spaces
        self.assertEqual(result.count(' '), 3)

class TestLeafNode(unittest.TestCase):
    def test_noprops(self):
    # Test a basic leaf node with tag and value
        node = LeafNode("p", "Hello, world!")
        self.assertEqual (node.to_html() == "<p>Hello, world!</p>")

    def test_notag(self):
    # Test a text-only node (no tag)
        text_node = LeafNode(None, "Just some text")
        self.assertEqual (text_node.to_html() == "Just some text")

    def test_novalue(self):
        try:
    # This should raise a ValueError
            bad_node = LeafNode("p", None)
            bad_node.to_html()
            self.assertRaises (False, "Should have raised ValueError")
        except ValueError:
            pass