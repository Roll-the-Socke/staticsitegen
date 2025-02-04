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

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        full_path = os.path.join(dir_path_content, file)
        rel_path = os.path.relpath(full_path, dir_path_content)
        dest_path = os.path.join(dest_dir_path, rel_path)
        if os.path.isfile(full_path):
            if full_path.endswith(".md"):
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)
                generate_page(full_path, template_path, dest_path)
        else:
            os.makedirs(dest_path, exist_ok=True)
            generate_page_recursive(full_path, template_path, dest_dir_path)
