import re


def remove_parentheses_and_punctuation(input_string):
    without_parentheses = re.sub(r'[()]', '', input_string)

    without_punctuation = re.sub(r'[^\w\s-]', ' ', without_parentheses)

    return without_punctuation


def space_the_parentheses(string: str):
    return re.sub(r'(\(|\))', r' \1 ', string)


