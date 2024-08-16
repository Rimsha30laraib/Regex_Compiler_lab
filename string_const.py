import re

# Pattern to match exactly the newline character '\n'
pattern = r'^\"(\\?[a-zA-Z_])*\"|\"(\\[\\|\'|\"])*\"$'

def match(text):
    if re.fullmatch(pattern, text):
        print("Valid character")
    else:
        print("Invalid character")

text = input("Enter a character: ")
match(text)
