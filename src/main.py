from textnode import *
from htmlnode import *
from markdowntransformation import *
from generator import generate_page, generate_pages_recursive
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
    
    # Paths for generate_pages_recursive
    content_dir = os.path.join(base_path, "content")  # Changed this to content directory
    template_file = os.path.join(base_path, "template.html")
    
    # Generate the HTML pages recursively
    generate_pages_recursive(content_dir, template_file, public_dir)  # Changed parameters

        
if __name__ == "__main__":
    main()