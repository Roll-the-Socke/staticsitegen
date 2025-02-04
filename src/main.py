from textnode import *
from htmlnode import *
from markdowntransformation import *
import os
import shutil

text = "this is text"
text_type = TextType.BOLD
url = "www.google.com"

def copy_static_to_public(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination)
    _recursive_copy(source, destination)


def _recursive_copy(source, destination):
    for item in os.listdir(source):
        full_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)
        print(f"Found item: {full_path}")
        if os.path.isfile(full_path):
            shutil.copy(full_path, dest_path)
            print(f"Copying file: {full_path} to {dest_path}")
        elif os.path.isdir(full_path):
            os.makedirs(dest_path)
            print(f"Created directory: {dest_path}")
            _recursive_copy(full_path, dest_path)


def main():
    source = os.path.expanduser("~/workspace/github.com/Roll-the-Socke/staticsitegen/static")
    destination = os.path.expanduser("~/workspace/github.com/Roll-the-Socke/staticsitegen/public")

    copy_static_to_public(source, destination)

        
if __name__ == "__main__":
    main()