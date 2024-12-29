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

