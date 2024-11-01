from enum import Enum

class TextType(Enum):
    NORMAL = "normal"
    BOLD   = "bold"
    ITALIC = "italic"
    CODE   = "code"
    LINK   = "link"
    IMAGE  = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.url = url
        self.text_type = TextType(text_type)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def __eq__(self, a, b):
        return a.text == b.text and a.url == b.url and a.text_type == b.text_type
