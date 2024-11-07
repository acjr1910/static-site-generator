import unittest
from extract_markdown_images import (
    extract_markdown_images,
)


class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        result_tuple = extract_markdown_images(text)
        [a, b] = result_tuple
        assert (a, ('rick roll', 'https://i.imgur.com/aKaOqIh.gif'))
        assert (b, ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg'))


if __name__ == "__main__":
    unittest.main()
