from collections import defaultdict

from morph_analyzer import morph_analyzer


def is_operator(token):
    return token in {'и', 'или', 'не'}


def get_operator_priority(operator):
    if operator == 'не':
        return 3
    elif operator == 'и':
        return 2
    elif operator == 'или':
        return 1
    else:
        return 0


def get_postfix_notation_and_words_to_search(tokens):
    words_to_search_dict = defaultdict(bool)

    output = []
    operators = []
    for token in tokens:
        if is_operator(token):
            while operators and get_operator_priority(operators[-1]) >= get_operator_priority(token):
                output.append(operators.pop())
            operators.append(token)
        elif token.isalnum():
            word_normal_form=morph_analyzer.parse(token)[0].normal_form
            output.append(word_normal_form)
            words_to_search_dict[word_normal_form] = False
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()

    while operators:
        output.append(operators.pop())
    # print(operators, output)
    # print(words_to_search_dict)
    return output, words_to_search_dict


def evaluate_postfix_notation(tokens,words_to_search):
    # print(tokens)
    stack = []
    for token in tokens:
        if is_operator(token):
            if token == 'и':
                operand2 = stack.pop()
                operand1 = stack.pop()
                # print(operand1, operand2)
                stack.append(operand1 and operand2)
            elif token == 'или':
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 or operand2)
            elif token == 'не':
                operand = stack.pop()
                stack.append(not operand)
        elif token.isalnum():
            stack.append(words_to_search[token])
    return stack[0]
