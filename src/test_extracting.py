import unittest
from markdowntransformation import extract_markdown_images, extract_markdown_links

class TestExtracting(unittest.TestCase):

    def test_empty_text(self):
        self.assertEqual(extract_markdown_images(""), [])
        self.assertEqual(extract_markdown_links(""), [])
    
    def test_single_image(self):
        text = "![alt text](https://example.com/image.jpg)"
        expected = [("alt text", "https://example.com/image.jpg")]
        self.assertEqual(extract_markdown_images(text), expected)
    
    def test_single_link(self):
        text = "Check out [my website](https://example.com)"
        expected = [("my website", "https://example.com")]
        self.assertEqual(extract_markdown_links(text), expected)

    def test_multiple_mixed(self):
        text = "Here's a ![cat](cat.jpg) and a [link](test.com) and another ![dog](dog.png)"
        self.assertEqual(
            extract_markdown_images(text), 
            [("cat", "cat.jpg"), ("dog", "dog.png")]
        )
        self.assertEqual(
            extract_markdown_links(text), 
            [("link", "test.com")]
        )

if __name__ == "__main__":
    unittest.main()