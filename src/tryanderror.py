def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text = node.text
            first_delimiter = text.find(delimiter)
            if first_delimiter != -1:
                second_delimiter = text.find(delimiter, first_delimiter + len(delimiter))
                if second_delimiter == -1:
                    raise Exception("Not a valid Markdown Text")
                first = TextNode(text[0:first_delimiter], TextType.TEXT)
                second = TextNode(text[first_delimiter + len(delimiter):second_delimiter], text_type)
                third = TextNode(text[second_delimiter + len(delimiter):], TextType.TEXT)
                new_nodes.extend([first, second, third])
    return new_nodes


node = TextNode("bla`code`bla", "`" ,TextType.TEXT)
print(split_nodes_delimiter(node))