from expression_processing_utils import get_postfix_notation_and_words_to_search, evaluate_postfix_notation
from morph_analyzer import morph_analyzer
from regex import remove_parentheses_and_punctuation, space_the_parentheses


def main():
    with open('input_text.txt', 'r', encoding='utf-8') as file:
        input_text = file.read()
    with open('input_expression.txt', 'r', encoding='utf-8') as file:
        input_expression = file.read()

    # убираем знаки препинания из исходного текста для удобства использования split
    input_text = remove_parentheses_and_punctuation(input_text).split()

    # добавляем пробелы вокруг скобок в логическом выражении, также для удобства использования split
    input_expression_tokens = space_the_parentheses(input_expression).split()

    # получаем массив с токенами в постфиксной форме и словарь нормальных форм слов, поиск которых необходимо осуществить
    postfix_representation, words_to_search = get_postfix_notation_and_words_to_search(input_expression_tokens)

    # создаем сет из всех возможных форм слов для поиска
    words_to_search_forms = set(form for word in words_to_search for form in morph_analyzer.get_all_forms(word))

    # проходим по словам в тексте, если слово есть вышеупомянутом сете - ставим метку True в соответствующем словаре
    for word in input_text:
        if word.lower() in words_to_search_forms:
            normal_form = morph_analyzer.parse(word)[0].normal_form
            words_to_search[normal_form] = True

    # вычисляем выражение в постфиксной форме, обращаясь к словарю words_to_search
    eval_result = evaluate_postfix_notation(postfix_representation, words_to_search)
    if eval_result:
        print('Текст удовлетворяет заданным условиям')
    else:
        print('Текст не удовлетворяет заданным условиям')


if __name__ == '__main__':
    main()
