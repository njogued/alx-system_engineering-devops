#!/usr/bin/python3

import re

txt = "She made us drinks to drink, we drunk them and got drunk"

text_searched = re.search(r"^She.*drunk$", txt)
if text_searched:
    print("We gottem boys")
else:
    print("They got away chief.")

'''
Flag r in re.search means raw text. Necessity?? Code also works without
The caret ^ expression matches the start of a string
The period . matches any character except new line
The asterisk * matches 0 or more repetitions ie, in *drunk it
    matches 0 or more of any character
The $ character matches the end'''

# E-mail validation
def validator(mail):
    # Assuming correct format is loremipsum@<provider>.com
    # 1. Must start with either A-Za-z0-9 => ^[A-Za-z0-9]
    valid = re.search("^[a-zA-Z0-9]", mail)
    if valid:
        print("Enter your password")
    else:
        print("Enter a valid e-mail address")

if __name__ == "__main__":
    mail = input("Enter your email: ")
    validator(mail)
