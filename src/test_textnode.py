import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, bold, None)")
        node = TextNode("This is a text node", TextType.ITALIC, "test.com")
        self.assertEqual(node.__repr__(), "TextNode(This is a text node, italic, test.com)")



if __name__ == "__main__":
    unittest.main()