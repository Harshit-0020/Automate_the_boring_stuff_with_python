import re


def regex_strip(text, character=''):
    # Regex to find white-spaces at the begnning and the en of the text.
    reg_strip = re.compile(r'(\s)*(.+)(\s)*')

    # Regex to find character in the text.
    char_strip_reg = re.compile(character)

    if not character:
        text = reg_strip.sub(r'\2', text)
    if character:
        text = char_strip_reg.sub(r'', text)
    print(text)
