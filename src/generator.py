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

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for file in files:
        full_path = os.path.join(dir_path_content, file)
        if os.path.isfile(full_path) and full_path.endswith(".md"):
            # Get relative path from content dir
            rel_path = os.path.relpath(full_path, dir_path_content)
            # Get directory name and create destination path
            dir_name = os.path.dirname(rel_path)
            # Create the destination directory path
            dest_dir = os.path.join(dest_dir_path, dir_name)
            # Ensure the directory exists
            os.makedirs(dest_dir, exist_ok=True)
            # Create path for index.html in that directory
            dest_html = os.path.join(dest_dir, "index.html")
            # Generate the page
            generate_page(full_path, template_path, dest_html)
        elif os.path.isdir(full_path):
            # Handle subdirectories
            subdir = os.path.basename(full_path)
            new_dest = os.path.join(dest_dir_path, subdir)
            generate_pages_recursive(full_path, template_path, new_dest)