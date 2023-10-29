#!/usr/bin/python3
"""Module that contains text_indentation function."""

def text_indentation(text):
    """
        prints a text with 2 new lines after each of these characters: ., ? and :

        Args:
            text (str): text to print

        Raises:
            TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    for d in ".?:":
        text = (d + "\n\n").join(
            (l.strip(" ") for l in text.split(d)))

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
