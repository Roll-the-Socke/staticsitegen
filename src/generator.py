from htmlnode import *
from textnode import *
from markdowntransformation import *
import os
import shutil

def generate_page(from_path, template_path, dest_path):
    
    with open(from_path, "r") as file:
        contents = file.read()
        
        html_node = markdown_to_html_node(contents)
        
        title = extract_title(contents)
    with open(template_path, "r") as file:
        template_contents = file.read()
        
        final_html = template_contents.replace("{{ Title }}", title)
        final_html = final_html.replace("{{ Content }}", html_node.to_html())

        os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w") as file:
        file.write(final_html)