import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode(tag="a", value="link string", props={ "href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.__repr__(), "tag: a, value: link string, children: None, props:  href=\"https://www.google.com\" target=\"_blank\"")


if __name__ == "__main__":
    unittest.main()