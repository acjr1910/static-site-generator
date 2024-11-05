class HTMLNode():
  def __init__(self, tag=None, value=None, props=[], children=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props
  
  def to_html(self):
    raise NotImplementedError()
  
  def props_to_html(self):
    props_string = ""
    for k in self.props:
      props_string += f" {k}=\"{self.props[k]}\""
    return props_string

  def __repr__(self):
    return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props_to_html()}"


class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=[]):
    super().__init__(tag, value, props, children=None)

  def to_html(self):
    if self.value == None:
      raise ValueError("All leaf nodes must have a value")
    if self.tag == None:
      return self.value
    else:
      return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
  def __init__(self, tag, children):
    super().__init__(tag, children=children)

  def to_html(self):
    if self.tag == None:
      raise ValueError("All parent nodes must have a tag")
    elif self.children == None:
      raise ValueError("All parent nodes must have children")
    
    def helper(children):
      if not children:
        return ""
      return children[0].to_html() + helper(children[1:])
    
    return f"<{self.tag}>{helper(self.children)}</{self.tag}>"
