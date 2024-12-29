import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


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
        node = LeafNode("p", "Hello, world!", None)
        self.assertEqual (node.to_html(), "<p>Hello, world!</p>")

    def test_notag(self):
    # Test a text-only node (no tag)
        text_node = LeafNode(None, "Just some text", None)
        self.assertEqual (text_node.to_html(), "Just some text")

    def test_novalue(self):
        try:
    # This should raise a ValueError
            bad_node = LeafNode("p", None)
            bad_node.to_html()
            self.assertRaises (False, "Should have raised ValueError")
        except ValueError:
            pass

class TestParentNode(unittest.TestCase):
    def test_simple(self):
        leaf = LeafNode("span", "Hello")
        assert leaf.to_html() == "<span>Hello</span>"

    def test_parent_multipleleaf(self):
        parent = ParentNode(
            "div",
            [
                LeafNode("p", "Paragraph 1"),
                LeafNode("p", "Paragraph 2")
            ]
        )
        assert parent.to_html() == "<div><p>Paragraph 1</p><p>Paragraph 2</p></div>"

    def test_nested_parents(self):
        nested_parent = ParentNode(
            "ul", 
            [
                ParentNode("li", [LeafNode(None, "Item 1")]),
                ParentNode("li", [LeafNode(None, "Item 2")])
            ]
        )
        assert nested_parent.to_html() == "<ul><li>Item 1</li><li>Item 2</li></ul>"

    def test_missing_parenttag(self):
        try:
            ParentNode(None, [LeafNode("b", "Text")]).to_html()
            assert False, "Expected ValueError for missing tag"
        except ValueError as e:
            assert str(e) == "mhh mhh tag is missing"

    def test_empty_children(self):
        try:
            ParentNode("div", []).to_html()
            assert False, "Expected ValueError for missing children"
        except ValueError as e:
            assert str(e) == "mhh mhh children is missing"