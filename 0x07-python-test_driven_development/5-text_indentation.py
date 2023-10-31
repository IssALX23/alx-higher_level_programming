#!/usr/bin/python3
"""
define function  that prints a text with 2 new lines after (. : ?)
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text: strings
    Return:
        print new text
    """
    # remove extra spaces from text
    words = text.split()
    text = ' '.join(words)

    # print text
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = ""

    for letter in text:
        if letter in ('.', '?', ':'):
            print(new_text.strip() + letter, end='\n\n')
            new_text = ""
        else:
            new_text += letter

    if new_text:
        print(new_text.strip(), end='')
