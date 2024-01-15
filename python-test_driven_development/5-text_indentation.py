#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Args:
        text (str): Input

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in '.:?':
        text = text.replace(char, char + '\n\n')

    print(*(ln.strip() for ln in (text + '\n').splitlines()), sep='\n', end='')
