class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        s = ""
        for key in self.props:
            s += f' {key}="{self.props[key]}"'
        return s
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag} value={self.value} children={self.children} props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tag:
            return f"{self.value}"
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("mhh mhh tag is missing")
        if not self.children:
            raise ValueError("mhh mhh children is missing")
        s = ""
        for child in self.children:
            s += f"{child.to_html()}"
        return f"<{self.tag}>{s}</{self.tag}>"

        