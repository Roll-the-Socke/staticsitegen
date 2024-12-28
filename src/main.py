from textnode import *

text = "this is text"
text_type = TextType.BOLD
url = "www.google.com"
def main():
    page = TextNode(text, text_type, url)
    print(page)

        
if __name__ == "__main__":
    main()