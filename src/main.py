from textnode import *
from htmlnode import *
from markdowntransformation import *
from generator import generate_page
import os
import shutil


def copy_static_to_public(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination)
    _recursive_copy(source, destination)


def _recursive_copy(source, destination):
    for item in os.listdir(source):
        full_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        
        if os.path.isfile(full_path):
            shutil.copy(full_path, dest_path)
            
        elif os.path.isdir(full_path):
            os.makedirs(dest_path)
            
            _recursive_copy(full_path, dest_path)


def main():
    # Set up base paths
    base_path = os.path.expanduser("~/workspace/github.com/Roll-the-Socke/staticsitegen")
    
    # Paths for copy_static_to_public
    static_dir = os.path.join(base_path, "static")
    public_dir = os.path.join(base_path, "public")
    
    # Copy static files
    copy_static_to_public(static_dir, public_dir)
    
    # Paths for generate_page
    markdown_file = os.path.join(base_path, "content/index.md")
    template_file = os.path.join(base_path, "template.html")
    output_file = os.path.join(public_dir, "index.html")
    
    # Generate the HTML page
    generate_page(markdown_file, template_file, output_file)

        
if __name__ == "__main__":
    main()